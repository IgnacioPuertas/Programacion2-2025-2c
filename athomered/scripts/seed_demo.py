from sqlmodel import Session, select
from app.infraestructura.bd import engine, inicializar_bd
from app.dominio.modelos import Usuario, Profesional
from app.nucleo.estrategias.contrasenia import construir_hasheador


def run():
    inicializar_bd()
    hasher = construir_hasheador()
    with Session(engine) as s:
        # familiares demo
        for name in ["maria", "jose", "ana"]:
            if not s.exec(
                select(Usuario).where(Usuario.username == name)
            ).first():
                s.add(
                    Usuario(
                        username=name,
                        password_hash=hasher.hash("password123"),
                        rol="familiar",
                    )
                )
                s.commit()

        # profesionales demo
        for uname, mat, esp, verif in [
            ("pro_1", "MAT-001", "AT", True),
            ("pro_2", "MAT-002", "Enfermeria", False),
        ]:
            u = s.exec(
                select(Usuario).where(Usuario.username == uname)
            ).first()
            if not u:
                u = Usuario(
                    username=uname,
                    password_hash=hasher.hash("password123"),
                    rol="profesional",
                )
                s.add(u)
                s.commit()
                s.refresh(u)
            p = s.exec(
                select(Profesional).where(Profesional.id_usuario == u.id)
            ).first()
            if not p:
                s.add(
                    Profesional(
                        id_usuario=u.id,
                        matricula=mat,
                        especialidad=esp,
                        verificado=verif,
                    )
                )
                s.commit()

    print(
        "Seed listo. Usuarios familiares: maria/jose/ana; profesionales: pro_1/pro_2; password para todos: password123"
    )


if __name__ == "__main__":
    run()
