from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True


class LoanBase(BaseModel):
    user_id: int
    book_id: int
    loan_date: date
    return_date: Optional[date] = None

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    user: User
    book: Book
    class Config:
        orm_mode = True

