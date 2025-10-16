from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.enrutador import api
from app.infraestructura.bd import inicializar_bd
from app.nucleo.observadores import registrar_observadores


@asynccontextmanager
async def vida(app: FastAPI):
    inicializar_bd()
    registrar_observadores()
    yield


app = FastAPI(title="AT home Red - API (MVP)", lifespan=vida)
app.include_router(api)


@app.get("/salud", tags=["monitor"])
def salud():
    return {"estado": "ok"}
