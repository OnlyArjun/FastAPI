from ast import Str
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class UserModel(BaseModel):
    id: Optional[UUID] = uuid4()
    firstName: str
    gender: str
