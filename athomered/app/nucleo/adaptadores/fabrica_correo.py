# from app.nucleo.adaptadores.correo_base import ClienteCorreo
# from app.nucleo.adaptadores.correo_consola import CorreoConsola
# from app.nucleo.adaptadores.correo_smtp import CorreoSMTP

import os
from .correo_base import ClienteCorreo
from .correo_consola import CorreoConsola

# correo_smtp es opcional: si no existe o falla al import, seguimos con consola
try:
    from .correo_smtp import CorreoSMTP
except Exception:
    CorreoSMTP = None  # type: ignore


def obtener_mailer() -> ClienteCorreo:
    """
    Devuelve una instancia de ClienteCorreo según MAIL_TRANSPORT.
    Si se pide 'smtp' pero falta el adaptador SMTP, vuelve a consola.
    """
    modo = os.getenv("MAIL_TRANSPORT", "console").lower()  # "console" | "smtp"
    if modo == "smtp" and CorreoSMTP is not None:
        # Si CorreoSMTP necesita configuración (host/port/user/pass), leerla aquí:
        # host = os.getenv("SMTP_HOST")
        # port = int(os.getenv("SMTP_PORT", "25"))
        # user = os.getenv("SMTP_USER")
        # password = os.getenv("SMTP_PASS")
        # return CorreoSMTP(host, port, user, password)
        return CorreoSMTP()  # mantener si el constructor no necesita params
    return CorreoConsola()
