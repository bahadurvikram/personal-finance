"""
This is a boilerplate pipeline 'linear_regression'
generated using Kedro 0.19.10
"""
import logging
from typing import Dict, Tuple
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def split_data(data: pd.DataFrame, target_data: pd.DataFrame, parameters: Dict[str, any]) -> Tuple:
    X = data
    y = target_data[parameters["target"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> Tuple:
    logger = logging.getLogger(__name__)
    y_pred = model.predict(X_test)
    logger.info(" target is %s", y_test.name)
    metrics = {
        "model_name": model.__class__.__name__,
        "r2_score": r2_score(y_test, y_pred),
        "mean_squared_error": mean_squared_error(y_test, y_pred)
    }
    logger.info("y_test %.3f min and %.3f max", y_test.min(), y_test.max())
    logger.info(" has a coefficient R^2 of %.3f on test data.", r2_score(y_test, y_pred))
    # Create the figure and axes objects
    fig, ax = plt.subplots(figsize=(6, 6))

    # Scatter plot of model predictions
    ax.scatter(y_test, y_pred, label="Model Predictions", color="red", s=10)

    # Line for y = x (perfect prediction line)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')

    # Set plot title and labels
    ax.set_title(f'Actual vs Predicted for {y_test.name}')
    ax.set_xlabel('Actual Values')
    ax.set_ylabel('Predicted Values')

    # Adjust layout
    plt.tight_layout()
    plt.close(fig)
    df = pd.DataFrame(list(metrics.items()), columns=["Metric", "Value"])
    return df, fig
