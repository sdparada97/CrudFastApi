from fastapi import APIRouter
from app.config.db import conn
from app.schemas.usuario import userEntity,usersEntity

usuario = APIRouter()

@usuario.post('/users')
def create_user():
    return {'message': 'Hello World'}

@usuario.get('/users')
def find_all_users():
    return {'message': 'Hello World'}

@usuario.get('/users/{id}')
def find_user():
    return {'message': 'Hello World'}

@usuario.put('/users')
def update_user():
    return {'message': 'Hello World'}

@usuario.delete('/users')
def delete_user():
    return {'message': 'Hello World'}
