from datetime import datetime
from pydantic import BaseModel


class Inventory(BaseModel):
    name: str
    quantity: int


class QuantityAdd(BaseModel):
    quantity: int

    class Config:
        orm_mode = True


class ShowInventory(BaseModel):
    name: str
    count: int
    issued: int
    date: datetime
    quantity: int

    class Config:
        orm_mode = True


class Student(BaseModel):
    name: str
    bookcount: int

    class Config:
        orm_mode = True


class ShowStudent(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PopularBook(BaseModel):
    name: str
    count: int

    class Config:
        orm_mode = True


class ManageInventory(BaseModel):
    b_id: int  # Inventory table b_id
    s_id: int  # Student table s_id
