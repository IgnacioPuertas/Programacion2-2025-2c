from abc import ABC, abstractmethod

# Ingredient products
class Dough:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sauce:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Cheese:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Clams:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# ╔═════════════════════════════════════════════╗
# ║ Paso 2.1 — Creamos las clases para los      ║
# ║ ingredientes nuevos (Veggies y Pepperoni).  ║
# ╚═════════════════════════════════════════════╝
class Veggies:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name
        
class Pepperoni:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...

# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ Paso 2.2 — Agregamos nuevos métodos abstractos                        ║
# ║ para crear los tipos de ingredientes (Veggies y Pepperoni).           ║
# ╚═══════════════════════════════════════════════════════════════════════╝
    @abstractmethod
    def create_Veggies(self) -> list["Veggies"]: ...
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni: ...


# ╔═══════════════════════════════════════════════════════════════════════╗
# ║ Paso 2.3 — Actualizamos las fábricas concretas:                       ║
# ║ Implementamos create_veggies( ) y create_pepperoni( ) en              ║
# ║ NYPizzaIngredientFactory y ChicagoPizzaIngredientFactory,             ║
# ║ devolviendo familias de ingredientes según la región.                 ║
# ╚═══════════════════════════════════════════════════════════════════════╝

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  
        return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  
        return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:
        return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Clams")

    def create_Veggies(self) -> list:
        return [Veggies("Garlic"), Veggies("Onion"), Veggies("Mushroom"), Veggies("Red Pepper")]
    
    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni("Sliced Pepperoni")


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  
        return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  
        return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:
        return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Frozen Clams")

    def create_Veggies(self) -> list:
        return [Veggies("Black Olives"), Veggies("Spinach"), Veggies("Eggplant")]
    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni("Sliced Pepperoni")
    
