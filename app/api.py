import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from titanic_model import __version__ as model_version
from titanic_model.predict import make_prediction

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/status", response_model=schemas.Status, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    status = schemas.Status(name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version)

    return status.dict()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleTitanicInputs) -> Any:
    """
    Make predictions on the survival probability of the Titanic passengers
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")

    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction result class: {results.get('preds')}")
    logger.info(f"Prediction result probability: {results.get('probs')}")

    return results
