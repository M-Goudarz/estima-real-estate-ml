import pandas as pd
from fastapi import FastAPI

from estima.model import load_model
from estima.schemas import HouseFeatures, PredictionResponse

app = FastAPI(
    title="Estima Real Estate Price Prediction API",
    description="API for predicting Tehran real estate prices.",
    version="1.0.0",
)

model = load_model()


@app.get("/health")
def health_check() -> dict[str, str]:
    """Check whether the API is running."""
    return {"status": "healthy"}


@app.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict_price(house: HouseFeatures) -> PredictionResponse:
    """Predict the price of a house."""
    house_data = pd.DataFrame([house.model_dump()])

    predicted_price = model.predict(house_data)[0]

    return PredictionResponse(
        predicted_price_toman=float(predicted_price),
    )