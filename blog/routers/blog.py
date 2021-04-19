from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, database
from blog.repository import blog_f
from blog.oath2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=list[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_f.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_f.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog,
                db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return blog_f.update(id, request, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,
           db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(get_current_user)):
    return blog_f.create(request, db)


@router.delete('/{id}')
def delete_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_f.delete(id, db)
