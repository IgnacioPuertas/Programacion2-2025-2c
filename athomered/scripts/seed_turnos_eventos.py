
"""
Crea turnos de ejemplo y dispara eventos para ver notificaciones en consola.

Ejecutar:
    python scripts/seed_turnos_eventos.py
"""
from datetime import datetime
import uuid
from sqlmodel import Session, select
from app.infraestructura.bd import engine, inicializar_bd
from app.dominio.modelos import Usuario, Profesional, Turno
from app.nucleo.observadores import registrar_observadores
from app.nucleo.eventos import bus, TurnoCreado
from app.nucleo.estrategias.contrasenia import construir_hasheador

def ensure_min_data(s):
    hasher = construir_hasheador()
    fam = s.exec(select(Usuario).where(Usuario.username == "familia_demo")).first()
    if not fam:
        fam = Usuario(username="familia_demo", password_hash=hasher.hash("password123"), rol="familiar")
        s.add(fam); s.commit(); s.refresh(fam)

    uprof = s.exec(select(Usuario).where(Usuario.username == "pro_demo")).first()
    if not uprof:
        uprof = Usuario(username="pro_demo", password_hash=hasher.hash("password123"), rol="profesional")
        s.add(uprof); s.commit(); s.refresh(uprof)

    prof = s.exec(select(Profesional).where(Profesional.id_usuario == uprof.id)).first()
    if not prof:
        prof = Profesional(id_usuario=uprof.id, matricula="MAT-999", especialidad="AT", verificado=True)
        s.add(prof); s.commit(); s.refresh(prof)

    return fam, prof

def run():
    inicializar_bd()
    registrar_observadores()

    with Session(engine) as s:
        fam, prof = ensure_min_data(s)

        for i in range(1, 3):
            t = Turno(
                id=str(uuid.uuid4()),
                id_paciente=fam.id,
                id_profesional=prof.id,
                estado="pendiente",
                creado_en=datetime.utcnow(),
            )
            s.add(t); s.commit(); s.refresh(t)
            bus.publicar(TurnoCreado(id_turno=t.id, id_paciente=t.id_paciente, id_profesional=t.id_profesional))
            print(f"[SEED] Turno creado #{i}: {t.id} -> estado={t.estado}")

    print("Listo. Usuarios: familia_demo / pro_demo (password: password123)")

if __name__ == "__main__":
    run()
