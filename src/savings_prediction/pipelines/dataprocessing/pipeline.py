"""
This is a boilerplate pipeline 'dataprocessing'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import one_hot_encoding, features_normalization

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=one_hot_encoding,
            inputs=["personal-finance", "params:col_options"],
            outputs="data_with_one_hot_encoding",
            name="handle_category_fields",
        ),
        node(
            func=features_normalization,
            inputs=["data_with_one_hot_encoding", "params:col_options"],
            outputs="data_with_normalization",
            name="handle_normalization",
        ),
    ])
