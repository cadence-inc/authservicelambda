from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from models.Contact import Contact
from models.Date import Date, date


account = {
    1: {
        "UID": 123,
        "name": "Michael",
        "location": "Orlando",
        "birthday": date,
        "phoneNumber": "123456789",
        "timezone": "ET",
        "isDelete": False
    }
}


class Account(BaseModel):
    UID: int
    name: str
    location: str
    birthday: Date
    phoneNumber: str
    timezone: str
    isDelete: bool


class UpdateAccount(BaseModel):
    UID: Optional[int] = None
    name: Optional[str] = None
    location: Optional[str] = None
    birthday: Optional[Date] = None
    phoneNumber: Optional[str] = None
    timezone: Optional[str] = None
    isDelete: Optional[bool] = None
