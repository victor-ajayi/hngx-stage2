from pydantic import BaseModel, Extra


class UserBase(BaseModel):
    id: int


class UserCreate(BaseModel):
    name: str

    class Config:
        extra = Extra.forbid


class UserUpdate(BaseModel):
    name: str

    class Config:
        extra = Extra.forbid


class User(UserBase):
    name: str

    class Config:
        orm_mode = True
