from typing import Optional, List

from pydantic import BaseModel


class ItemBaseSchema(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemSchema(ItemBaseSchema):
    id: int
    owner_id: Optional[int] = None

    class Config:
        orm_mode = True


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    hashed_password: str


class UserOutSchema(UserBaseSchema):
    id: int
    is_active: bool
    items: List[ItemSchema] = []

    class Config:
        orm_mode = True


class UserUpdateSchema(UserCreateSchema):
    is_active: bool
    items: List[ItemSchema] = []

    class Config:
        orm_mode = True


class UserSchema(UserUpdateSchema, UserOutSchema):
    pass
