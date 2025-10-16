"""
Acepta o rechaza el primer turno pendiente y dispara evento de notificación al paciente.

Uso:
    python scripts/accion_turnos_eventos.py aceptar
    python scripts/accion_turnos_eventos.py rechazar
"""

import sys
from sqlmodel import Session, select
from app.infraestructura.bd import engine, inicializar_bd
from app.dominio.modelos import Turno
from app.nucleo.observadores import registrar_observadores
from app.nucleo.eventos import bus, TurnoActualizado


def run(accion: str):
    if accion not in {"aceptar", "rechazar"}:
        print("Acción inválida. Usar: aceptar | rechazar")
        return

    inicializar_bd()
    registrar_observadores()
    with Session(engine) as s:
        t = s.exec(select(Turno).where(Turno.estado == "pendiente")).first()
        if not t:
            print("No hay turnos pendientes.")
            return
        t.estado = "aceptado" if accion == "aceptar" else "rechazado"
        s.add(t)
        s.commit()
        s.refresh(t)
        bus.publicar(
            TurnoActualizado(
                id_turno=t.id,
                id_paciente=t.id_paciente,
                id_profesional=t.id_profesional,
                nuevo_estado=t.estado,
            )
        )
        print(f"[ACCION] Turno {t.id} -> {t.estado}")


if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else "aceptar"
    run(accion)
