import uuid
from pydantic import BaseModel
import uuid
from datetime import datetime
from typing import Optional

class BookModel(BaseModel) :
    id : uuid.UUID
    title : str
    author: str
    genre: str
    price: float
    published_year: int
    available: bool
    created_at : datetime
    updated_at : datetime

class BookCreateModel(BaseModel):
    title: str
    author: str
    genre: str
    price: float
    published_year: int
    available: bool

class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    price: Optional[float] = None
    published_year: Optional[int] = None
    available: Optional[bool] = None