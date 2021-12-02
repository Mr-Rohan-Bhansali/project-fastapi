from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from project.helper.student import add_student, all_student, get_student
from project import schema
from project.orm.database import get_db
router = APIRouter(prefix='/student', tags=['Student'])


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schema.Student)
def create_student(r_body: schema.ShowStudent, db: Session = Depends(get_db)):
    return add_student(r_body, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.Student)
def get_one(id: int, db: Session = Depends(get_db)):
    return get_student(id, db)

@router.get('', response_model=List[schema.Student])
def get_all(db: Session = Depends(get_db)):
    return all_student(db)
