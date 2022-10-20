from uuid import uuid4
from fastapi import FastAPI
from typing import List
from models import UserModel

firstApp = FastAPI()

dbInstance: List[UserModel] = [
    UserModel(id=uuid4(), firstName="Arjun", gender="Male"),
    UserModel(id=uuid4(), firstName="Yadav", gender="Male")
]

#   async will help u wait the function
#   for a while to perform other functions
#   define the function as async and then
#   after writing await perform the other function


@firstApp.get("/")
def homeRoute():
    return {"Hello": "FASTApi"}


@firstApp.get("/api/users")
async def getUsersRoute():
    return dbInstance


@firstApp.post("/api/users")
async def addUsersRoute(givenUser: UserModel):
    dbInstance.append(givenUser)
    return {"id": givenUser.id}
