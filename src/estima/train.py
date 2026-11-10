import pandas as pd
from catboost import CatBoostRegressor


CATEGORICAL_FEATURES = ["Address"]


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> CatBoostRegressor:
    """Train the CatBoost model on the training dataset."""

    model = CatBoostRegressor(
        learning_rate=0.05,
        l2_leaf_reg=3,
        iterations=800,
        depth=8,
        loss_function="RMSE",
        random_seed=42,
        verbose=0,
    )

    model.fit(
        X_train,
        y_train,
        cat_features=CATEGORICAL_FEATURES,
    )

    return model