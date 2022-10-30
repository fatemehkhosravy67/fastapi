import peewee
from database import db
from pydantic import BaseModel, Field, EmailStr

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    hashed_password = peewee.CharField()
    is_active = peewee.BooleanField(default=False)
    is_admin = peewee.BooleanField(default=False)

    class Meta:
        database = db



class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "fatemeh khosravy",
                "email": "ftmkhosravy@gmail.com",
                "password": "1234@Sky"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "ftmkhosravy@gmail.com",
                "password": "1234@Sky"
            }
        }