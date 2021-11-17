import uvicorn
from fastapi import FastAPI


from app.routes import book_router
from app.routes import author_router

PROJECT_NAME = "BookstoreCRUDFastAPI"

app = FastAPI(
    title=PROJECT_NAME
)

if __name__ == '__main__':
    app.include_router(book_router, prefix="/api/book", tags=["book"])
    app.include_router(author_router, prefix="/api/author", tags=["author"])

    @app.get("/")
    def home():
        return {"message": "Welcome to FastAPI CRUD Example."}


    if __name__ == '__main__':
        uvicorn.run("main:app", host="127.0.0.1", port=8000)
