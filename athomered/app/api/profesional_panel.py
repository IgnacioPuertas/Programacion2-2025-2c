from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import List
from sqlmodel import Session, select
from app.infraestructura.bd import obtener_sesion
from app.dominio.modelos import Profesional, Turno
from app.nucleo.eventos import bus, TurnoActualizado

router = APIRouter()


class AltaPerfil(BaseModel):
    id_usuario: str
    matricula: str = Field(min_length=4)
    especialidad: str = "AT"
    zona: str | None = None


@router.post("/registro/alta-perfil")
def alta_perfil(datos: AltaPerfil, sesion: Session = Depends(obtener_sesion)):
    prof = sesion.exec(
        select(Profesional).where(Profesional.id_usuario == datos.id_usuario)
    ).first()
    if not prof:
        raise HTTPException(404, "Profesional no encontrado")
    prof.matricula = datos.matricula
    prof.especialidad = datos.especialidad
    sesion.add(prof)
    sesion.commit()
    sesion.refresh(prof)
    return {"ok": True, "id_profesional": prof.id}


class DisponibilidadIn(BaseModel):
    id_profesional: str
    disponible: bool


@router.patch("/agenda/disponibilidad")
def disponibilidad(
    datos: DisponibilidadIn, sesion: Session = Depends(obtener_sesion)
):
    prof = sesion.get(Profesional, datos.id_profesional)
    if not prof:
        raise HTTPException(404, "Profesional no encontrado")
    prof.verificado = datos.disponible
    sesion.add(prof)
    sesion.commit()
    return {"ok": True, "disponible": prof.verificado}


class TurnoOut(BaseModel):
    id: str
    id_paciente: str
    estado: str


@router.get("/agenda/pendientes", response_model=List[TurnoOut])
def pendientes(id_profesional: str, sesion: Session = Depends(obtener_sesion)):
    items = sesion.exec(
        select(Turno).where(
            (Turno.id_profesional == id_profesional)
            & (Turno.estado == "pendiente")
        )
    ).all()
    return [
        TurnoOut(id=t.id, id_paciente=t.id_paciente, estado=t.estado)
        for t in items
    ]


class DecidirTurnoIn(BaseModel):
    id_turno: str
    decision: str = Field(pattern="^(aceptar|rechazar)$")


@router.patch("/agenda/turno/decidir")
def decidir_turno(
    datos: DecidirTurnoIn, sesion: Session = Depends(obtener_sesion)
):
    t = sesion.get(Turno, datos.id_turno)
    if not t:
        raise HTTPException(404, "Turno no encontrado")
    t.estado = "aceptado" if datos.decision == "aceptar" else "rechazado"
    sesion.add(t)
    sesion.commit()
    sesion.refresh(t)
    bus.publicar(
        TurnoActualizado(
            id_turno=t.id,
            id_paciente=t.id_paciente,
            id_profesional=t.id_profesional,
            nuevo_estado=t.estado,
        )
    )
    return {"id": t.id, "estado": t.estado}


class HistorialOut(BaseModel):
    id: str
    id_paciente: str
    estado: str


@router.get("/agenda/historial", response_model=List[HistorialOut])
def historial(id_profesional: str, sesion: Session = Depends(obtener_sesion)):
    items = sesion.exec(
        select(Turno).where(Turno.id_profesional == id_profesional)
    ).all()
    return [
        HistorialOut(id=t.id, id_paciente=t.id_paciente, estado=t.estado)
        for t in items
    ]
