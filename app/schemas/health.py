from pydantic import BaseModel


class Status(BaseModel):
    name: str
    api_version: str
    model_version: str
