from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session
from app.infraestructura.bd import obtener_sesion
from app.dominio.modelos import Profesional

router = APIRouter()


class VerificarIn(BaseModel):
    id_profesional: str
    verificado: bool


@router.patch("/verificar")
def verificar(datos: VerificarIn, sesion: Session = Depends(obtener_sesion)):
    p = sesion.get(Profesional, datos.id_profesional)
    if not p:
        raise HTTPException(404, "Profesional no encontrado")
    p.verificado = datos.verificado
    sesion.add(p)
    sesion.commit()
    return {"ok": True, "id_profesional": p.id, "verificado": p.verificado}
