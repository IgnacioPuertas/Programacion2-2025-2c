# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_size(self) -> str:
        return self._beverage.get_size()

    @abstractmethod
    def get_description(self) -> str:
        pass

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        extras = {"Tall": 0.10, "Grande": 0.15, "Venti": 0.20}
        # Si no se encuentra el tamaño, se cobra el extra mínimo - Tall
        extra = extras.get(self.get_size(), 0.10) 
        return self._beverage.cost() + extra

class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramelo a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + 0.25


# class PrettyPrintDecorator(CondimentDecorator):
#     """
#     Decorador de presentación: transforma descripciones repetidas en 'Double', 'Triple', etc.
#     No afecta el costo, solo el texto.
#     """

#     def get_description(self) -> str:
#         desc = self._beverage.get_description()
#         parts = [p.strip() for p in desc.split(",")]

#         # contamos ocurrencias en orden de aparición
#         pretty_parts = []
#         seen = set()
#         for p in parts:
#             if p in seen:
#                 continue
#             count = parts.count(p)
#             if count == 1:
#                 pretty_parts.append(p)
#             elif count == 2:
#                 pretty_parts.append(f"Double {p}")
#             elif count == 3:
#                 pretty_parts.append(f"Triple {p}")
#             else:
#                 pretty_parts.append(f"{count}x {p}")
#             seen.add(p)

#         return ", ".join(pretty_parts)

#     def cost(self) -> float:
#         # No modifica el precio, solo pasa el costo de la bebida envuelta
#         return self._beverage.cost()
