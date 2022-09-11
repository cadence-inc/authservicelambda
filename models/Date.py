from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

date = {
    1: {
        "month": 9,
        "date": 3,
        "year": 2000,
    }
}


class Date(BaseModel):
    month: int
    date: int
    year: int


class UpdateDate(BaseModel):
    month: Optional[int] = None
    date: Optional[int] = None
    year: Optional[int] = None
