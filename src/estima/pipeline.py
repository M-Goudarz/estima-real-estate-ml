from estima.data import load_data, split_data
from estima.train import train_model
from estima.evaluate import evaluate_model
from estima.model import save_model


def run_training_pipeline() -> dict[str, float]:
    """Run the complete model training and evaluation pipeline."""

    df = load_data()

    X_train, X_test, y_train, y_test = split_data(df)

    model = train_model(X_train, y_train)

    metrics = evaluate_model(
        model=model,
        X_test=X_test,
        y_test=y_test,
    )

    save_model(model)

    return metrics