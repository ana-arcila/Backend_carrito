from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from config.mogo_db import collection
from models.carrodat_models import CarroDataGET
import json  # Import json module

router = APIRouter()

def parse_mongo_document(document):
    return {
        "_id": str(document["_id"]),
        "Angulo": str(document["Angulo"]),
        "Medidas": json.loads(document["Medidas"]),  # Parse Medidas as a list
        "x": str(document["x"]),
        "y": str(document["y"]),
    }

import logging

logging.basicConfig(level=logging.DEBUG)

@router.get("/all/", tags=["Sensor Data"], response_model=list[CarroDataGET])
def get_all_sensordata():
    try:
        cursor = collection.find({})
        data = [parse_mongo_document(doc) for doc in cursor]
        return data
    except Exception as e:
        logging.error("An error occurred while fetching sensor data: %s", str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})

