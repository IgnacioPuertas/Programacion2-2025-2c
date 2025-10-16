from app.nucleo.eventos import bus, TurnoCreado, TurnoActualizado
from app.nucleo.adaptadores.fabrica_correo import obtener_mailer
from app.nucleo.adaptadores.correo_base import ClienteCorreo

mailer: ClienteCorreo = obtener_mailer()


def _al_crear_turno(evt: TurnoCreado) -> None:
    asunto = "Nueva solicitud de turno"
    cuerpo = f"Turno #{evt.id_turno} solicitado por paciente {evt.id_paciente}"
    mailer.enviar(to=str(evt.id_profesional), asunto=asunto, cuerpo=cuerpo)


def _al_actualizar_turno(evt: TurnoActualizado) -> None:
    asunto = f"Tu turno cambió de estado a: {evt.nuevo_estado}"
    cuerpo = f"Turno #{evt.id_turno} con profesional {evt.id_profesional} ahora está '{evt.nuevo_estado}'"
    mailer.enviar(to=str(evt.id_paciente), asunto=asunto, cuerpo=cuerpo)


def registrar_observadores() -> None:
    bus.suscribir(TurnoCreado, _al_crear_turno)
    bus.suscribir(TurnoActualizado, _al_actualizar_turno)
