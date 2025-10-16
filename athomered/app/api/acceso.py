from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlmodel import Session, select
from app.infraestructura.bd import obtener_sesion
from app.dominio.modelos import Usuario, Profesional
from app.nucleo.estrategias.contrasenia import construir_hasheador

router = APIRouter()
_hasher = construir_hasheador()


class Registro(BaseModel):
    username: str = Field(min_length=3, max_length=32)
    password: str = Field(min_length=8, max_length=128)
    rol: str = Field(pattern="^(profesional|familiar)$")


@router.post("/registro")
def registro(datos: Registro, sesion: Session = Depends(obtener_sesion)):
    u = datos.username.strip().lower()
    if sesion.exec(select(Usuario).where(Usuario.username == u)).first():
        raise HTTPException(400, "Ese nombre de usuario ya existe")
    user = Usuario(
        username=u, password_hash=_hasher.hash(datos.password), rol=datos.rol
    )
    sesion.add(user)
    sesion.commit()
    sesion.refresh(user)
    if datos.rol == "profesional":
        prof = Profesional(id_usuario=user.id)
        sesion.add(prof)
        sesion.commit()
    return {"id": user.id, "username": user.username, "rol": user.rol}


class Login(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(datos: Login, sesion: Session = Depends(obtener_sesion)):
    u = datos.username.strip().lower()
    user = sesion.exec(select(Usuario).where(Usuario.username == u)).first()
    if not user or not _hasher.verificar(datos.password, user.password_hash):
        raise HTTPException(401, "Credenciales inválidas")
    return {"id": user.id, "username": user.username, "rol": user.rol}
