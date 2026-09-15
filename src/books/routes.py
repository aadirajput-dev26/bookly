from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.books.schema import BookModel, BookCreateModel, BookUpdateModel
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from .service import BookService
from typing import List
import uuid

book_router = APIRouter()
book_service = BookService()

@book_router.get('/', response_model=List[BookModel], status_code=status.HTTP_200_OK)
async def list_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.list_all_books(session)
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=BookModel)
async def create_book(books_data : BookCreateModel, session : AsyncSession = Depends(get_session)) -> dict :
    new_book = await book_service.create_book(books_data, session)
    return new_book

@book_router.get('/{book_id}', status_code=status.HTTP_200_OK, response_model=BookModel)
async def get_book(book_id : uuid.UUID, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_id, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")

@book_router.patch('/{book_id}', status_code = status.HTTP_200_OK, response_model=BookModel)
async def update_book(book_id : uuid.UUID, books_data : BookUpdateModel, session: AsyncSession = Depends(get_session)) -> dict :
    updated_book = await book_service.update_book(book_id, books_data, session)
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")\

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: uuid.UUID, session: AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_id, session)
    if deleted_book:
        return None
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Book ID not found")