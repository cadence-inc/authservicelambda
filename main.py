from dotenv import load_dotenv
import os


from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

from models.Date import Date, date, UpdateDate
from models.Contact import Contact, contact, UpdateContact
from models.Cadence import Cadence, cadence, UpdateCadence
from models.Account import Account, account, UpdateAccount

app = FastAPI()


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


'''
- /getContactsByUID
    - In: UID
    - Out: List<Contact Objects>
'''

# don't test it


@app.get("/getContactsByUID")
def get_contact_uid(uid: int):
    for contact_id in contact:
        if account[contact_id]["UID"] == uid:
            return contact[contact_id]["connection"]
        return {"Data": "Not Found"}


'''
- /getAccountInfoByUID
    - in: UID
    - out: AccountModel
'''


@app.get("/getAccountInfoByUID")
def get_accountInfoByUID(uid: int):
    for account_id in account:
        if account[account_id]["UID"] == uid:
            return account[account_id]
    return {"Account": "Not Found"}


#  ------------------------ create Method -------------------------

@app.post("/create-date/{date_id}")
def create_date(date_id: int, day: Date):
    if date_id in date:
        return {"Error": "Date has already exists"}

    date[date_id] = day
    return date[date_id]


'''
- /addNewContact
    - in:  uid1, uid2,
    - out: confirmation: boolean
    - also: create the new contact record, set null for cadence
    @contact_id: id of the host user
    @user: add new one
'''


@app.post("/addNewContact/{contact_id}")
def create_contact(contact_id: int, user: Contact):
    if contact_id in contact:
        return False
    contact[contact_id] = user
    return True


'''
@app.post("/create-cadence/{cadence_id}")
def create_cadence(cadence_id: int, user: Cadence):
    if cadence_id in cadence:
        return {"Error": "Cadence has already exists"}
    cadence[cadence_id] = user

    return cadence[cadence_id]
'''


'''
- /setNewCadence
    - In: Contact ID: String, NewInterval: Int
    - Out: confirmation: boolean
    - also: create new cadence record if no cadence yet and add to contact, update next meeting
    this is create a new Cadence in case we don't have a Cadence yet

'''


@app.post("/setNewCadence{cadence_id}")
def set_newCadence(cadence_id: int, user: Cadence):
    confirmation = False
    if cadence_id in cadence:
        # Cadence already exist -> need to update (put method)
        return confirmation
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
def update_contact(contact_id: int, user: UpdateContact):
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


'''
- /setNewCadence
    - In: Contact ID: String, NewInterval: Int (/put)
    - Out: confirmation: boolean
    - also: create new cadence record(post method) if no cadence yet and add to contact, update next meeting
    UPDATE Cadence: user can chose any information they want to update
'''


@app.put("/update-cadence/{cadence_id}")
def update_cadence(cadence_id: int, user: UpdateCadence):
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


'''
- /updateAccountInfo
    - in:  uid, name:String, birthday: DateTime?, #homecity: String?
    - out: isUpdateSuccessful: boolean
'''


@app.put("/updateAccountInfo/{account_id}")
def update_account(account_id: int, user: UpdateAccount):
    if account_id not in account:
        account[account_id].isUpdateSuccessful = False
        return account[account_id].isUpdateSuccessful

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
    if user.isUpdateSuccessful != None:
        account[account_id].isUpdateSuccessful = user.isUpdateSuccessful
        account[account_id].isUpdateSuccessful = True

    return account[account_id].isUpdateSuccessful


'''
@app.put("updateAccountInfo/{account_id}")
def update_account_info(account_id: int, user: UpdateAccount):
    if account_id not in account:
        #account[account_id].isUpdateSuccessful = False
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
    if user.isUpdateSuccessful != None:
        account[account_id].isUpdateSuccessful = user.isUpdateSuccessful
        #account[account_id].isUpdateSuccessful = True
    return account[account_id]
'''
