from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas, database
from blog.repository import user_f

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user_f.get(id, db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user_f.create(request, db)
