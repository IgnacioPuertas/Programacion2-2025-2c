from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import List
from sqlmodel import Session, select
from datetime import datetime
import uuid

from app.infraestructura.bd import obtener_sesion
from app.dominio.modelos import Profesional, Turno
from app.nucleo.eventos import bus, TurnoCreado

router = APIRouter()


class ProfesionalOut(BaseModel):
    id: str
    especialidad: str
    verificado: bool


@router.get("/busqueda", response_model=List[ProfesionalOut])
def buscar_profesionales(
    especialidad: str | None = None, sesion: Session = Depends(obtener_sesion)
):
    q = select(Profesional)
    if especialidad:
        q = q.where(Profesional.especialidad == especialidad)
    items = sesion.exec(q).all()
    return [
        ProfesionalOut(
            id=p.id, especialidad=p.especialidad, verificado=p.verificado
        )
        for p in items
    ]


class SolicitarTurnoIn(BaseModel):
    id_paciente: str
    id_profesional: str


@router.post("/turnos/solicitar")
def solicitar_turno(
    datos: SolicitarTurnoIn, sesion: Session = Depends(obtener_sesion)
):
    if not sesion.get(Profesional, datos.id_profesional):
        raise HTTPException(404, "Profesional inexistente")
    t = Turno(
        id=str(uuid.uuid4()),
        id_paciente=datos.id_paciente,
        id_profesional=datos.id_profesional,
        estado="pendiente",
        creado_en=datetime.utcnow(),
    )
    sesion.add(t)
    sesion.commit()
    bus.publicar(
        TurnoCreado(
            id_turno=t.id,
            id_paciente=t.id_paciente,
            id_profesional=t.id_profesional,
        )
    )
    return {"id": t.id, "estado": t.estado}


class ConfirmarCancelarIn(BaseModel):
    id_turno: str
    accion: str = Field(pattern="^(confirmar|cancelar)$")


@router.patch("/turnos/estado")
def cambiar_estado_turno(
    datos: ConfirmarCancelarIn, sesion: Session = Depends(obtener_sesion)
):
    t = sesion.get(Turno, datos.id_turno)
    if not t:
        raise HTTPException(404, "Turno no encontrado")
    t.estado = "aceptado" if datos.accion == "confirmar" else "cancelado"
    sesion.add(t)
    sesion.commit()
    return {"id": t.id, "estado": t.estado}
