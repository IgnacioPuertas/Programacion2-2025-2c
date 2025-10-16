from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session
from app.infraestructura.bd import obtener_sesion
from app.dominio.modelos import Usuario

router = APIRouter()


class MiUsuario(BaseModel):
    id: str
    username: str
    rol: str


@router.get("/mi-usuario", response_model=MiUsuario)
def mi_usuario(id_usuario: str, sesion: Session = Depends(obtener_sesion)):
    u = sesion.get(Usuario, id_usuario)
    if not u:
        raise HTTPException(404, "Usuario no encontrado")
    return MiUsuario(id=u.id, username=u.username, rol=u.rol)


@router.post("/suscripcion")
def suscripcion(id_usuario: str, plan: str):
    return {
        "ok": True,
        "id_usuario": id_usuario,
        "plan": plan,
        "nota": "mock de suscripción",
    }


@router.post("/contacto")
def contacto(tema: str, mensaje: str):
    return {"ok": True, "ticket": "SOP-" + tema[:3].upper() + "-0001"}


@router.post("/cerrar-sesion")
def cerrar_sesion():
    return {"ok": True}
