# app/nucleo/adaptadores/correo_consola.py
#from .correo_base import ClienteCorreo  # <-- import relativo

#class CorreoConsola(ClienteCorreo):
#    """Adapter de desarrollo: imprime 'emails' en consola."""
#    def enviar(self, to: str, asunto: str, cuerpo: str) -> None:
#        print(f"[EMAIL -> {to}] {asunto}\n{cuerpo}")


from .correo_base import ClienteCorreo  # import relativo

class CorreoConsola(ClienteCorreo):
    """Adapter de desarrollo: imprime 'emails' en consola."""
    def enviar(self, to: str, asunto: str, cuerpo: str) -> None:
        print(f"[EMAIL -> {to}] {asunto}\n{cuerpo}")
