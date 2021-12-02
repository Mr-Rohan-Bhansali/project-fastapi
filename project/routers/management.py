from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from project.helper.management import allotBook, get_management, returnBook, top_5_book
from project import schema
from project.orm.database import get_db
router = APIRouter(prefix='/manage', tags=['Management'])


@router.get('/management', status_code=status.HTTP_200_OK, response_model=List[schema.ShowManagement])
def all_management(db: Session = Depends(get_db)):
    return get_management(db)


@router.post('/allot', status_code=status.HTTP_201_CREATED)
def allot_book(r_body: schema.ManageInventory, db: Session = Depends(get_db)):
    return allotBook(r_body, db)


@router.get('/popular_books', status_code=status.HTTP_200_OK, response_model=List[schema.PopularBook])
def popular_book(db: Session = Depends(get_db)):
    return top_5_book(db)


@router.post('/return', status_code=status.HTTP_202_ACCEPTED)
def ret_book(r_body: schema.ManageInventory, db: Session = Depends(get_db)):
    return returnBook(r_body, db)
