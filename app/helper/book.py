from datetime import datetime
from fastapi.exceptions import HTTPException
from starlette import status

from app.orm.models import Inventory


def add_book(r_body, db):
    bookAdded = Inventory(
        name=r_body.name, quantity=r_body.quantity, date=datetime.now())
    db.add(bookAdded)
    db.commit()
    db.refresh(bookAdded)
    return bookAdded


def all_book(db):
    blogs = db.query(Inventory).all()
    return blogs


def get_book(id, db):
    blog = db.query(Inventory).filter(Inventory.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with id {id} is not available')
    return blog


def update_book(id, r_body, db):
    query = db.query(Inventory).filter(Inventory.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Bookid with {id} is not found')
    a = query.update(
        {'quantity': query.first().quantity+r_body.quantity})
    db.commit()
    query = db.query(Inventory.name, Inventory.quantity).filter(
        Inventory.id == id).first()
    return query


# def del_book(id, db):
#     d = db.query(Books).filter(Books.id == id)
#     if not d.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Invalid book id {id}')
#     d.delete(synchronize_session=False)
#     db.commit()
#     return {'status': 'deleted successfully'}
