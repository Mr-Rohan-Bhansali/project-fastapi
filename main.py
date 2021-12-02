from fastapi import FastAPI
from project.orm.models import Base
from project.orm.database import engine
from project.routers import book, management, student
app = FastAPI()
Base.metadata.create_all(engine)


app.include_router(book.router)
app.include_router(student.router)
app.include_router(management.router)
