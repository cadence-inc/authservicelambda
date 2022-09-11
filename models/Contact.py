from models.Date import Date, date
from models.Cadence import Cadence, cadence
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union, Optional
from models.Account import Account, account

contact = {
    1: {
        "cadenceID": 100,
        "cadence": cadence,
        "connection": [account.keys()],
        "Date_Add": date,
        "isDelete": False
    }


}


class Contact(BaseModel):
    # cadence ID: int
    cadenceID: int = None
    # map: user1, user2
    cadence: Cadence
    connection: list[int]
    Date_Add: Date
    isDelete: bool


class UpdateContact(BaseModel):
    cadenceID: Optional[int] = None
    cadence: Optional[Cadence] = None
    connection: Optional[list[int]] = None
    Date_Add: Optional[Date] = None
    isDelete: Optional[bool] = None
