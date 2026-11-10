from pathlib import Path

from catboost import CatBoostRegressor


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "catboost_model.cbm"


def save_model(model: CatBoostRegressor) -> None:
    """Save the trained CatBoost model."""

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    model.save_model(str(MODEL_PATH))


def load_model() -> CatBoostRegressor:
    """Load a trained CatBoost model."""

    model = CatBoostRegressor()
    model.load_model(str(MODEL_PATH))

    return model