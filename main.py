from fastapi import FastAPI
from app.orm.models import Base
from app.orm.database import engine
from app.routers import book, management, student
app = FastAPI()
Base.metadata.create_all(engine)


app.include_router(book.router)
app.include_router(student.router)
app.include_router(management.router)
