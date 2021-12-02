from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import and_
from starlette import status
from project.orm.models import Inventory, Student, Management


def allotBook(r_body, db):
    student = db.query(Student).filter(
        Student.id == r_body.s_id)
    student1 = student.first()
    book = db.query(Inventory).filter(Inventory.id == r_body.b_id)
    book1 = book.first()
    p_count = book1.count
    a = db.query(Management).filter(
        and_(Management.b_id == r_body.b_id, Management.s_id == r_body.s_id)).first()
    if not a:
        if student1.bookcount < 3:
            if book1.quantity-book1.issued > 0:
                p_count += 1
                allot = Management(date=datetime.now(),
                                   b_id=r_body.b_id, s_id=r_body.s_id)
                student1.bookcount += 1
                book1.issued += 1
                book1.count += 1
                db.add(allot)
                db.commit()
                db.refresh(allot)
                return "alloted"
            return "Not available in Libary"
        return f"Already have {student1.bookcount} books"
    return "already issued"


def top_5_book(db):
    user = db.query(Inventory).order_by(Inventory.count.desc()).limit(5).all()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid id {id}')
    return user


def returnBook(r_body, db):
    student = db.query(Student).filter(
        Student.id == r_body.s_id)
    student1 = student.first()
    book = db.query(Inventory).filter(Inventory.id == r_body.b_id)
    book1 = book.first()
    a = db.query(Management).filter(
        and_(Management.b_id == r_body.b_id, Management.s_id == r_body.s_id))
    b = a.first()
    if b:
        a.update({'ret': 1})
        a.date = datetime.now()
        student1.bookcount -= 1
        book1.issued -= 1
        book1.date = datetime.now()
        db.commit()
        return 'returned successfully'
    return 'first issue the book'
