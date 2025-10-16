
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Dict, List, Type

@dataclass
class EventoDominio:
    ts: datetime = datetime.utcnow()

@dataclass
class TurnoCreado(EventoDominio):
    id_turno: str = ""
    id_paciente: str = ""
    id_profesional: str = ""

@dataclass
class TurnoActualizado(EventoDominio):
    id_turno: str = ""
    id_paciente: str = ""
    id_profesional: str = ""
    nuevo_estado: str = ""  # aceptado | rechazado | cancelado | etc.

class BusEventos:
    def __init__(self) -> None:
        self._subs: Dict[Type, List[Callable]] = {}
    def suscribir(self, tipo_evento: Type, manejador: Callable) -> None:
        self._subs.setdefault(tipo_evento, []).append(manejador)
    def publicar(self, evento: EventoDominio) -> None:
        for manejador in self._subs.get(type(evento), []):
            manejador(evento)

bus = BusEventos()
