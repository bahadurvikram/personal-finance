"""
This is a boilerplate pipeline 'linear_regression'
generated using Kedro 0.19.10
"""
from kedro.pipeline import Pipeline, pipeline, node

from .nodes import evaluate_model, train_model, split_data

def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = pipeline([
        node(
            func=split_data,
            inputs=["data_with_normalization", "data_targets", "params:model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node",

        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="regressor",
            name="train_model_node",
        ),
        node(
            func=evaluate_model,
            inputs=["regressor", "X_test", "y_test"],
            outputs=["linear_model_metrics","linear_data_and_predictions_plot"],
            name="evaluate_model_node",
        ),
    ])

    # any inputs and outputs defined here will not be parametrized
    ds_pipeline_1 = pipeline(
        pipe=pipeline_instance,
        inputs=["data_with_normalization", "data_targets"],
        namespace="target1_modelling_pipeline"
    )
    # ds_pipeline_2 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target2_modelling_pipeline"
    # )
    # ds_pipeline_3 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target3_modelling_pipeline"
    # )
    # ds_pipeline_4 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target4_modelling_pipeline"
    # )
    # ds_pipeline_5 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target5_modelling_pipeline"
    # )
    # ds_pipeline_6 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target6_modelling_pipeline"
    # )
    # ds_pipeline_7 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target7_modelling_pipeline"
    # )
    # ds_pipeline_8 = pipeline(
    #     pipe=pipeline_instance,
    #     inputs=["data_with_normalization", "data_targets"],
    #     namespace="target8_modelling_pipeline"
    # )

    # return ds_pipeline_1+ds_pipeline_2+ds_pipeline_3+ds_pipeline_4+ds_pipeline_5+ds_pipeline_6+ds_pipeline_7+ds_pipeline_8
    return ds_pipeline_1