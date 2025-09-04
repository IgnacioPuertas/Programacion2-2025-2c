# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    SIZES = ("Tall", "Grande", "Venti")

    def __init__(self, size: str = "Tall"):
        self.description = "Bebida Desconocida"
        self._size = size

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description

    def get_size(self) -> str:
        """
        Devuelve el tamaño de la bebida.
        """
        return self._size

    def set_size(self, size: str) -> None:
        """Establece el tamaño de la bebida."""
        if size not in Beverage.SIZES:
            raise ValueError(f"Tamaño inválido: {size}. Use uno de {Beverage.SIZES}")
        self._size = size

    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass

# --- Componentes Concretos ---
class HouseBlend(Beverage):
    def __init__(self, size: str = "Tall"):
        super().__init__(size=size)
        self.description = "Café de la Casa"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self, size: str = "Tall"):
        super().__init__(size=size)
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    def __init__(self, size: str = "Tall"):
        super().__init__(size=size)
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        return 1.05


class Espresso(Beverage):
    def __init__(self, size: str = "Tall"):
        super().__init__(size=size)
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99