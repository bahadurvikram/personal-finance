"""
This is a boilerplate pipeline 'lgbm_regression'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, split_data, tune_hyperparameters
from ..linear_regression.nodes import evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = pipeline([
        node(
            func=split_data,
            inputs=["data_normalized_type_categorised", "data_targets", "params:model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node",

        ),
        node(
            func=tune_hyperparameters,
            inputs=["X_train", "y_train", "params:model_options"],
            outputs="best_params",
            name="hyperparameter_tuning_node"
        ),

        node(
            func=train_model,
            inputs=["X_train", "y_train", "best_params", "params:model_options"],
            outputs="lgbm_regressor",
            name="train_model_node",
        ),
        node(
            func=evaluate_model,
            inputs=["lgbm_regressor", "X_test", "y_test"],
            outputs=["lgbm_model_metrics", "lgbm_data_and_predictions_plot"],
            name="evaluate_model_node",
        ),
    ])

    # any inputs and outputs defined here will not be parametrized
    ds_pipeline_1 = pipeline(
        pipe=pipeline_instance,
        inputs=["data_normalized_type_categorised", "data_targets"],
        namespace="target1_lgbm_pipeline"
    )
    return ds_pipeline_1