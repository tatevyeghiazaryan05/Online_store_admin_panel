from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime


class AdminLoginSchema(BaseModel):
    email: EmailStr
    password: str


class DrinkSchema(BaseModel):
    name: str
    kind: str
    price: float
    category: str
    image: str


class DrinkNameChangeSchema(BaseModel):
    name: str


class DrinkKindChangeSchema(BaseModel):
    kind: str


class DrinkPriceChangeSchema(BaseModel):
    price: float


class DrinkCategoryChangeSchema(BaseModel):
    category: str


class DrinkImageChangeSchema(BaseModel):
    image: str


class AdminPasswordRecover(BaseModel):
    code: int
    new_password: str


class GetFeedbacksSchema(BaseModel):
    start_date: datetime.date
    end_date: datetime.date
