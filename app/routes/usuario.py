from typing import List
from fastapi import APIRouter, Response, status
from app.config.db import User
from app.models.usuario import Usuario
from app.schemas.usuario import userEntity, usersEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

usuario = APIRouter()

@usuario.post("/users", response_model=Usuario, tags=["Usuarios"])
def create_user(user: Usuario):
    new_user = dict(user)
    id_new_user = User.insert_one(new_user).inserted_id

    user = User.find_one({"_id": id_new_user})

    return userEntity(user)


@usuario.get("/users", response_model=List[Usuario], tags=["Usuarios"])
def find_all_users():
    return usersEntity(User.find())


@usuario.get("/users/{id}", response_model=Usuario, tags=["Usuarios"])
def find_user(id: str):
    return userEntity(User.find_one({"_id": ObjectId(id)}))


@usuario.put("/users/{id}", response_model=Usuario, tags=["Usuarios"])
def update_user(id: str, user: Usuario):
    User.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(User.find_one({"_id": ObjectId(id)}))


@usuario.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def delete_user(id: str):
    userEntity(User.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
