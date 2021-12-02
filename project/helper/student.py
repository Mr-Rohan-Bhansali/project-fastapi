from fastapi.exceptions import HTTPException
from starlette import status
from project.orm.models import Student


def add_student(r_body, db):
    student = Student(name=r_body.name, bookcount=0)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student(id, db):
    user = db.query(Student).filter(Student.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid student id:{id}')
    return user


def all_student(db):
    student = db.query(Student).all()
    return student
