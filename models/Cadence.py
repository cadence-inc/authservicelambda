from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from models.Date import Date


class Cadence(BaseModel):
    interval: int
    mostRecentMeeting: Date
    dateAdded: Date
    isDelete: bool


cadence = {
    1: {
        "interval": 0,
        "mosRecentMeeting": 1,
        "dateAdded": 1,
        "isDelete": False
    }
}


class UpdateCadence(BaseModel):
    interval: Optional[int] = None
    mostRecentMeeting: Optional[Date] = None
    dateAdded: Optional[Date] = None
    isDelete: Optional[bool] = None
