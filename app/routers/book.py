from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from app import schema
from app.helper.book import add_book, all_book, get_book, update_book
from app.orm.database import get_db
router = APIRouter(tags=['Book'], prefix='/book')


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schema.ShowInventory)
def add_book_inv(r_body: schema.Inventory, db: Session = Depends(get_db)):
    return add_book(r_body, db)


@router.get('', response_model=List[schema.ShowInventory])
def get_all(db: Session = Depends(get_db)):
    return all_book(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowInventory)
def get_one(id: int, db: Session = Depends(get_db)):
    return get_book(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED,response_model=schema.Inventory)
def updateBlog(id: int, r_body: schema.QuantityAdd, db: Session = Depends(get_db)):
    return update_book(id, r_body, db)


# @router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def delete(id, db: Session = Depends(get_db)):
#     return del_book(id, db)