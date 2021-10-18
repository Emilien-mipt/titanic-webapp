from typing import Any, List, Optional

from pydantic import BaseModel
from titanic_model.processing.validation import TitanicInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    preds: Optional[List[int]]
    probs: Optional[List[float]]


class MultipleTitanicInputs(BaseModel):
    inputs: List[TitanicInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "PassengerId": 0,
                        "Pclass": 1,
                        "Name": "Snyder, Mrs. John Pillsbury (Nelle Stevenson)",
                        "Sex": "female",
                        "Age": 23,
                        "SibSp": 1,
                        "Parch": 0,
                        "Ticket": 21228,
                        "Fare": 82.2667,
                        "Cabin": "B45",
                        "Embarked": "S",
                    }
                ]
            }
        }
