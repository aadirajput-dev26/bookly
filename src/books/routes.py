from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.books_data import books
from src.books.schema import book_model

book_router = APIRouter()

@book_router.get('/', status_code=status.HTTP_200_OK)
async def list_all_books():
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(books_data : book_model) -> dict :
    books.append(books_data.model_dump())
    return books_data.model_dump()

@book_router.get('/{book_id}')
async def get_book(book_id : int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")

@book_router.patch('/{book_id}', status_code = status.HTTP_200_OK)
async def update_book(books_data : book_model) -> dict :
    books_data = books_data.model_dump()

    for book in books:
        if book["id"] == books_data["id"] :
            book["title"] = books_data["title"]
            book["author"] = books_data["author"]
            book["genre"] = books_data["genre"]
            book["price"] = books_data["price"]
            book["published_year"] = books_data["published_year"]
            book["available"] = books_data["available"]

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")\

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Book ID not found")