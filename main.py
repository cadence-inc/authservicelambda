from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from models.Date import Date, date, UpdateDate
from models.Contact import Contact, contact, UpdateContact
from models.Cadence import Cadence, cadence, UpdateCadence
from models.Account import Account, account, UpdateAccount

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

#  ------------------------ get Method -------------------------


@app.get("/get-date/{date_id}")
def get_date(date_id: int):
    if date_id not in date:
        return {"Error": "Date doesn't exist"}
    return date[date_id]


@app.get("/get-contact/{contact_id}")
def get_contact(contact_id: int):
    if contact_id not in contact:
        return {"Error": "Contact doesn't exist"}
    return contact[contact_id]


@app.get("/get-account/{account_id}")
def get_account(account_id: int):
    if account_id not in account:
        return {"Data": "Not Found"}
    return account[account_id]


#  ------------------------ create Method -------------------------

@app.post("/create-date/{date_id}")
def create_date(date_id: int, day: Date):
    if date_id in date:
        return {"Error": "Date has already exists"}

    date[date_id] = day
    return date[date_id]


@app.post("/create-contact/{contact_id}")
def create_contact(contact_id: int, user: Contact):
    if contact_id in contact:
        return {"Error": "Contact has already exists"}
    contact[contact_id] = user
    return contact[contact_id]


@app.post("/create-cadence/{cadence_id}")
def create_cadence(cadence_id: int, user: Cadence):
    if cadence_id in cadence:
        return {"Error": "Cadence has already exists"}
    cadence[cadence_id] = user

    return cadence[cadence_id]


@app.post("/create-account{account_id}")
def create_account(account_id: int, user: Account):
    if account_id in account:
        return {"Error": "Account has already exists"}
    account[account_id] = user
    return account[account_id]

#  ------------------------ update Method -------------------------


@app.put("/update-date/{date_id}")
def update_date(date_id: int, day: UpdateDate):
    if date_id not in date:
        return {"Error": "Date ID does not exists"}

    if day.month != None:
        date[date_id].month = day.month
    if day.date != None:
        date[date_id].date = day.date
    if day.year != None:
        date[date_id].year = day.year
    return date[date_id]


@app.put("/update-contact/{contact_it}")
def update(contact_id: int, user: UpdateContact):
    if contact_id not in contact:
        return {"Error": "Contact ID does not exists"}

    if user.cadence != None:
        contact[contact_id].cadence = user.cadence
    if user.Date_Add != None:
        contact[contact_id].Date_Add = user.Date_Add
    if user.name != None:
        contact[contact_id].name = user.name
    if user.isDelete != None:
        contact[contact_id].isDelete = user.isDelete

    return contact[contact_id]


@app.put("/update-cadence/{cadence_id}")
def update(cadence_id: int, user: UpdateCadence):
    if cadence_id not in cadence:
        return {"Error": "Cadence ID does not exists"}

    if user.interval != None:
        cadence[cadence_id].interval = user.interval
    if user.mostRecentMeeting != None:
        cadence[cadence_id].mostRecentMeeting = user.mostRecentMeeting
    if user.dateAdded != None:
        cadence[cadence_id].dateAdded = user.dateAdded
    if user.isDelete != None:
        cadence[cadence_id].isDelete = user.isDelete

    return cadence[cadence_id]


@app.put("/update-account/{account_id}")
def update(account_id: int, user: UpdateAccount):
    if account_id not in account:
        return {"Error": "Account ID does not exists"}

    if user.UID != None:
        account[account_id].UID = user.UID
    if user.name != None:
        account[account_id].name = user.name
    if user.location != None:
        account[account_id].location = user.location
    if user.birthday != None:
        account[account_id].birthday = user.birthday
    if user.phoneNumber != None:
        account[account_id].phoneNumber = user.phoneNumber
    if user.timezone != None:
        account[account_id].timezone = user.timezone
    if user.isDelete != None:
        account[account_id].isDelete = user.isDelete

    return account[account_id]
