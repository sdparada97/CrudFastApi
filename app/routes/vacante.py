from typing import List
from fastapi import APIRouter, Response, status
from app.config.db import Vacancy
from app.models.vacante import Vacante
from app.schemas.vacante import vacancyEntity, vacanciesEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

vacante = APIRouter()


@vacante.post("/vacancies", response_model=Vacante, tags=["Vacantes"])
def create_vacancy(user: Vacante):
    new_vacancy = dict(user)
    id_new_vacancy = Vacancy.insert_one(new_vacancy).inserted_id

    vacancy = Vacancy.find_one({"_id": id_new_vacancy})

    return vacancyEntity(vacancy)


@vacante.get("/vacancies", response_model=List[Vacante], tags=["Vacantes"])
def find_all_vacancies():
    return vacanciesEntity(Vacancy.find())


@vacante.get("/vacancies/{id}", response_model=Vacante, tags=["Vacantes"])
def find_vacancy(id: str):
    return vacancyEntity(Vacancy.find_one({"_id": ObjectId(id)}))


@vacante.put("/vacancies/{id}", response_model=Vacante, tags=["Vacantes"])
def update_user(id: str, vacancy: Vacante):
    Vacancy.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(vacancy)})
    return vacancyEntity(Vacancy.find_one({"_id": ObjectId(id)}))


@vacante.delete("/vacancies/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Vacantes"])
def delete_vacancy(id: str):
    vacancyEntity(Vacancy.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
