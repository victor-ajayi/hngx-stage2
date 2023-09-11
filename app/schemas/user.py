from pydantic import BaseModel


class UserBase(BaseModel):
    id: int


class UserCreate(BaseModel):
    name: str


class UserUpdate(BaseModel):
    name: str


class UserRequest(BaseModel):
    name: str


class User(UserBase):
    name: str

    class Config:
        orm_mode = True
