"""
This is a boilerplate pipeline 'dataprocessing'
generated using Kedro 0.19.10
"""
import logging
import pandas as pd
from typing import Dict

from sklearn.preprocessing import StandardScaler, OneHotEncoder


def one_hot_encoding(df: pd.DataFrame, parameters: Dict[str, any]) -> pd.DataFrame:
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    encoded_cats = encoder.fit_transform(df[parameters["categorical_features"]])
    encoded_cat_columns = encoder.get_feature_names_out(parameters["categorical_features"])

    df_encoded_cats = pd.DataFrame(encoded_cats, columns=encoded_cat_columns)
    data_with_one_hot_encoding = pd.concat([df[parameters["numerical_features"]+parameters["variable_expenses"]],  df_encoded_cats], axis=1)
    return data_with_one_hot_encoding

def features_normalization(df: pd.DataFrame, parameters: Dict[str, any]) -> pd.DataFrame:
    data_with_normalization = df
    scaler = StandardScaler()

    scaled_numerical = scaler.fit_transform(df[parameters["numerical_features"]+parameters["variable_expenses"]])

    df_scaled_numerical = pd.DataFrame(scaled_numerical, columns=parameters["numerical_features"]+parameters["variable_expenses"], index=df.index)

    data_with_normalization.update(df_scaled_numerical)
    return data_with_normalization
