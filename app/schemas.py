from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    email: EmailStr
    posts: List["Post"] = []

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    text: str = Field(..., max_length=1048576)



class PostCreate(PostBase):
    pass
    

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
