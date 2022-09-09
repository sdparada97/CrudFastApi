from fastapi import FastAPI
from app.routes.usuario import usuario
from app.routes.vacante import vacante

app = FastAPI(
    title="REST API Usuarios-Vacantes"
)

app.include_router(usuario)
app.include_router(vacante)