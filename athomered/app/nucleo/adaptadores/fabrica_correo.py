
import os
from app.nucleo.adaptadores.correo_base import ClienteCorreo
from app.nucleo.adaptadores.correo_consola import CorreoConsola
from app.nucleo.adaptadores.correo_smtp import CorreoSMTP

#def obtener_mailer() -> ClienteCorreo:
#    modo = os.getenv("MAIL_TRANSPORT", "console").lower()  # console | smtp
#    if modo == "smtp":
#        return CorreoSMTP()
#    return CorreoConsola()


import os
from .correo_base import ClienteCorreo           # import relativo
from .correo_consola import CorreoConsola        # import relativo

# correo_smtp es opcional: si no existe o falla, seguimos con consola
try:
    from .correo_smtp import CorreoSMTP          # import relativo
except Exception:
    CorreoSMTP = None  # type: ignore

def obtener_mailer() -> ClienteCorreo:
    modo = os.getenv("MAIL_TRANSPORT", "console").lower()  # console | smtp
    if modo == "smtp" and CorreoSMTP is not None:
        return CorreoSMTP()
    return CorreoConsola()
