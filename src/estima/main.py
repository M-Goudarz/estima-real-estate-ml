from estima.pipeline import run_training_pipeline


def main() -> None:
    """Run the training pipeline and print evaluation metrics."""

    metrics = run_training_pipeline()

    print("\nModel Evaluation Results")
    print("-" * 30)

    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:,.2f}")


if __name__ == "__main__":
    main()