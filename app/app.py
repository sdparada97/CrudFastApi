from fastapi import FastAPI
from app.routes.usuario import usuario

app = FastAPI()

app.include_router(usuario)