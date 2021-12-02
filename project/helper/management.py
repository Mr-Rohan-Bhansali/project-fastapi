from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import and_
from starlette import status
from project.orm.models import Inventory, Student, Management


def allotBook(r_body, db):
    student = db.query(Student).filter(
        Student.id == r_body.s_id)
    student1 = student.first()
    if student1 == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    book = db.query(Inventory).filter(Inventory.id == r_body.b_id)
    book1 = book.first()
    if book1 == None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='book not available')
    p_count = book1.count
    a = db.query(Management).filter(
        and_(Management.b_id == r_body.b_id, Management.s_id == r_body.s_id, Management.ret == False))
    c = None
    if a.first() != None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="already issued")
    else:
        b = a.first()
    if (not b):
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
                raise HTTPException(status_code=status.HTTP_200_OK,
                                    detail="alloted")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not available in Libary")
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Already have {student1.bookcount} books")
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="already issued")


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
    if student1 == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    book = db.query(Inventory).filter(Inventory.id == r_body.b_id)
    book1 = book.first()
    if book1==None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='book not available')
    a = db.query(Management).filter(
        and_(Management.b_id == r_body.b_id, Management.s_id == r_body.s_id,Management.ret==False))
    b = a.first()
    if b==None:
        raise HTTPException(
        status_code=status.HTTP_208_ALREADY_REPORTED, detail='first issue the book')
    else:
        a.update({'ret': True})
        returned = Management(date=datetime.now(),
                                b_id=r_body.b_id, s_id=r_body.s_id, ret=True)
        db.add(returned)
        student1.bookcount -= 1
        book1.issued -= 1
        book1.date = datetime.now()
        db.commit()
        return 'returned successfully'
    


def get_management(db):
    query = db.query(Management).all()
    return query
