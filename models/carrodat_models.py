# carrodat_models.py
from pydantic import BaseModel
from typing import List

class CarroDataGET(BaseModel):
    _id: str
    Angulo: float
    Medidas: List[float]
    x: float
    y: float
