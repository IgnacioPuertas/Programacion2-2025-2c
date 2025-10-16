import os
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///athomered.db")
connect_args = (
    {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def inicializar_bd() -> None:
    from app.dominio.modelos import Usuario, Profesional, Turno

    SQLModel.metadata.create_all(engine)


def obtener_sesion():
    with Session(engine) as sesion:
        yield sesion
