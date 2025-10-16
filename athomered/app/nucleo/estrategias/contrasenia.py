
import os
from abc import ABC, abstractmethod
from passlib.context import CryptContext

class HasheadorContrasenia(ABC):
    @abstractmethod
    def hash(self, texto: str) -> str: ...
    @abstractmethod
    def verificar(self, texto: str, hash_guardado: str) -> bool: ...

class HasheadorArgon2(HasheadorContrasenia):
    def __init__(self) -> None:
        self._ctx = CryptContext(schemes=["argon2"], deprecated="auto")
    def hash(self, texto: str) -> str: return self._ctx.hash(texto)
    def verificar(self, texto: str, hash_guardado: str) -> bool: return self._ctx.verify(texto, hash_guardado)

class HasheadorBcrypt(HasheadorContrasenia):
    def __init__(self) -> None:
        self._ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    def hash(self, texto: str) -> str: return self._ctx.hash(texto)
    def verificar(self, texto: str, hash_guardado: str) -> bool: return self._ctx.verify(texto, hash_guardado)

def construir_hasheador() -> HasheadorContrasenia:
    algo = os.getenv("PWD_ALGO", "argon2").lower()
    return HasheadorArgon2() if algo == "argon2" else HasheadorBcrypt()
