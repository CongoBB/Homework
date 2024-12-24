from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def get_all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.is_active == True)).all()
    return users


@router.get('/user_id')
async def get_user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='There is no such user')
    return user


@router.get('/user_id/tasks')
async def get_tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='There is no such user')
    tasks = db.scalar(select(Task).where(Task.user_id == user_id)).all()
    if len(tasks) == 0:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='No tasks for such user')
    return tasks

@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username),
                                   is_active=True))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No such user found')

    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age,
    ))

    db.commit()

    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User data has been updated successfully'}

@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            'No such user found')
    db.execute(delete(User).where(User.id == user_id))
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    for task in tasks:
        db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User has been successfully deleted'}


