from pydantic import BaseModel

class book_model(BaseModel) :
    id : int
    title : str
    author: str
    genre: str
    price: float
    published_year: int
    available: bool

