from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is running ....")
    await init_db()
    yield
    print("Server has been stopped !!")

app = FastAPI(lifespan=life_span)

@app.get('/')
async def health_route() -> dict:
    return {
        "success" : True,
        "message" : "Server is running ...."
    }

app.include_router(book_router, prefix="/api/v1/books")