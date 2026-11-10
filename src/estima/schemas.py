from pydantic import BaseModel, Field


class HouseFeatures(BaseModel):
    """Input features for house price prediction."""

    Area: int = Field(gt=0, description="House area in square meters")
    Room: int = Field(ge=0, description="Number of rooms")
    Parking: bool
    Warehouse: bool
    Elevator: bool
    Address: str = Field(min_length=1, description="House neighborhood")


class PredictionResponse(BaseModel):
    """Response containing the predicted house price."""

    predicted_price_toman: float = Field(
        gt=0,
        description="Predicted house price in Toman",
    )