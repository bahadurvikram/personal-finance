"""
This is a boilerplate pipeline 'lgbm_regression'
generated using Kedro 0.19.10
"""

import logging
from typing import Dict, Tuple

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import lightgbm as lgb
import pandas as pd


def split_data(data: pd.DataFrame, target_data: pd.DataFrame, parameters: Dict[str, any]) -> Tuple:
    logger = logging.getLogger(__name__)
    X = data
    y = target_data[parameters["target"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def tune_hyperparameters(X_train: pd.DataFrame, y_train: pd.Series, parameters: Dict[str, any]) -> dict:
    model = lgb.LGBMRegressor(random_state=42)

    # Define the hyperparameter grid
    param_grid = parameters["prams"]

    # Perform grid search
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring="r2", n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # Return the best hyperparameters
    return grid_search.best_params_


def train_model(X_train: pd.DataFrame, y_train: pd.Series, best_params: dict, parameters: Dict[str, any]) -> lgb.LGBMRegressor:
    model = lgb.LGBMRegressor(random_state=42, **best_params)
    model.fit(X_train, y_train)
    return model
