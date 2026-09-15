from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

class Book(SQLModel, table = True) :
    __tablename__ = "books"

    id : uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    title : str
    author: str
    genre: str
    price: float
    published_year: int
    available: bool
    created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<Book Title> : {self.title}"