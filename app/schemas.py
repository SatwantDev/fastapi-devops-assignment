from pydantic import BaseModel, EmailStr
from datetime import datetime


# ---------- USER ----------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


# ---------- NOTE ----------

class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True        