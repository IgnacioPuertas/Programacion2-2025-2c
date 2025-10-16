# app/nucleo/adaptadores/correo_smtp.py
import os
import smtplib
from email.message import EmailMessage
from .correo_base import ClienteCorreo  # <-- import relativo

class CorreoSMTP(ClienteCorreo):
    """Adapter SMTP sencillo (usa smtplib)."""
    def __init__(self) -> None:
        self.host = os.getenv("SMTP_HOST", "localhost")
        self.port = int(os.getenv("SMTP_PORT", "587"))
        self.username = os.getenv("SMTP_USER", "")
        self.password = os.getenv("SMTP_PASS", "")
        self.use_tls = os.getenv("SMTP_TLS", "true").lower() in ("1","true","yes","on")
        self.sender = os.getenv("SMTP_FROM", self.username or "no-reply@example.com")

    def enviar(self, to: str, asunto: str, cuerpo: str) -> None:
        msg = EmailMessage()
        msg["From"] = self.sender
        msg["To"] = to
        msg["Subject"] = asunto
        msg.set_content(cuerpo)

        with smtplib.SMTP(self.host, self.port) as smtp:
            if self.use_tls:
                smtp.starttls()
            if self.username:
                smtp.login(self.username, self.password)
            smtp.send_message(msg)
