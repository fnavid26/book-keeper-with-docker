from sqlalchemy import Column, Integer, String,Date,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, nullable=True)

    loans = relationship("Loan", back_populates="book")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    loans = relationship("Loan", back_populates="user")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    loan_date = Column(Date)
    return_date = Column(Date, nullable=True)

    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")
