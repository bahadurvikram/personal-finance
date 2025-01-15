"""
This is a boilerplate pipeline 'dataprocessing'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import features_processing, features_aggregator

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=features_processing,
            inputs=["personal-finance", "params:col_options"],
            outputs={
                    "one_hot_encoded_data": "one_hot_encoded_data",
                    "normalized_data": "normalized_data",
                    "categorised_data": "categorised_data",
                    "data_targets": "data_targets",
                },
            name="handle_features_processing",
        ),
        node(
            func=features_aggregator,
            inputs=["one_hot_encoded_data", "normalized_data", "categorised_data"],
            outputs=["data_with_normalization","data_normalized_type_categorised"],
            name="handle_data_aggregation",
        ),
    ])
