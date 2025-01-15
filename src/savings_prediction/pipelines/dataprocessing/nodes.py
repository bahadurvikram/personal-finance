"""
This is a boilerplate pipeline 'dataprocessing'
generated using Kedro 0.19.10
"""
import logging
import pandas as pd
from typing import Dict, Tuple

from sklearn.preprocessing import StandardScaler, OneHotEncoder


def features_processing(df: pd.DataFrame, parameters: Dict[str, any]) -> dict:
    # Applying one hot encoding
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    encoded_cats = encoder.fit_transform(df[parameters["categorical_features"]])
    encoded_cat_columns = encoder.get_feature_names_out(parameters["categorical_features"])
    df_encoded_cats = pd.DataFrame(encoded_cats, columns=encoded_cat_columns)
    # Applying normalization
    scaler = StandardScaler()
    scaled_numerical = scaler.fit_transform(df[parameters["features"]])
    df_scaled_numerical = pd.DataFrame(scaled_numerical, columns=parameters["features"], index=df.index)
    # Applying category type changes
    df_cats = pd.DataFrame(df[parameters["categorical_features"]], columns=parameters["categorical_features"])
    for category in parameters["categorical_features"]:
        df_cats[category] = df_cats[category].astype('category')

    data_targets = df[parameters["targets"]]
    return {"one_hot_encoded_data": df_encoded_cats,
            "normalized_data": df_scaled_numerical,
            "categorised_data": df_cats,
            "data_targets": data_targets
            }


def features_aggregator(df_encoded: pd.DataFrame, df_normalized: pd.DataFrame, df_categorized: pd.DataFrame) -> Tuple:
    logger = logging.getLogger(__name__)
    normalized_encoded_aggregated_date = pd.concat([df_normalized, df_encoded], axis=1)
    logger.info(" now normalized_encoded_aggregated_date cols are %s", normalized_encoded_aggregated_date.columns)
    normalized_type_categorized_aggregated_date = pd.concat([df_normalized, df_categorized], axis=1)
    logger.info(" now normalized_type_categorized_aggregated_date cols are %s", normalized_type_categorized_aggregated_date.columns)
    return normalized_encoded_aggregated_date, normalized_type_categorized_aggregated_date