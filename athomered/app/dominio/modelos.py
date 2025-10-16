from datetime import datetime
from sqlmodel import SQLModel, Field
import uuid


def _uuid() -> str:
    return str(uuid.uuid4())


class Usuario(SQLModel, table=True):
    id: str = Field(default_factory=_uuid, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    password_hash: str
    rol: str = Field(default="familiar")
    creado_en: datetime = Field(default_factory=datetime.utcnow)


class Profesional(SQLModel, table=True):
    id: str = Field(default_factory=_uuid, primary_key=True)
    id_usuario: str = Field(foreign_key="usuario.id", index=True)
    matricula: str | None = Field(default=None, index=True)
    especialidad: str = "AT"
    verificado: bool = Field(default=False)


class Turno(SQLModel, table=True):
    id: str = Field(default_factory=_uuid, primary_key=True)
    id_paciente: str = Field(foreign_key="usuario.id", index=True)
    id_profesional: str = Field(foreign_key="profesional.id", index=True)
    estado: str = Field(default="pendiente")
    creado_en: datetime = Field(default_factory=datetime.utcnow)
