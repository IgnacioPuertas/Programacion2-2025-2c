# app/nucleo/adaptadores/correo_base.py
from abc import ABC, abstractmethod


class ClienteCorreo(ABC):
    """Interfaz del Adapter de correo."""

    @abstractmethod
    def enviar(self, to: str, asunto: str, cuerpo: str) -> None: ...
