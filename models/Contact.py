from models.Date import Date
from models.Cadence import Cadence, cadence
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union, Optional

contact = {
    1: cadence

}


class Contact(BaseModel):
    cadence: Cadence
    name: list[str]
    Date_Add: Date
    isDelete: bool


class UpdateContact(BaseModel):
    cadence: Optional[Cadence] = None
    name: Optional[list[str]] = None
    Date_Add: Optional[Date] = None
    isDelete: Optional[bool] = None
