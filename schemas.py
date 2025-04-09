from pydantic import BaseModel, EmailStr


class AdminLoginSchema(BaseModel):
    email: EmailStr
    password: str


class DrinkSchema(BaseModel):
    name: str
    kind: str
    price: float
    image: str


class DrinkNameChangeSchema(BaseModel):
    name: str