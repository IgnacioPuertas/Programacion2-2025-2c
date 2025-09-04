from beverages import Beverage
from condiments import Milk, Mocha, Soy, Whip, Caramel

def build_beverage(base: Beverage, size: str, condiments: list[str]) -> Beverage:
    """
    Construye una bebida a partir de:
      - una base (Espresso, HouseBlend, etc.)
      - un tamaño (Tall, Grande, Venti)
      - una lista de condimentos en forma de strings

    Ejemplo:
        build_beverage(Espresso(), Beverage.S_GRANDE, ["soy", "mocha", "whip"])
    """
    base.set_size(size)

    mapping = {
        "milk": Milk,
        "mocha": Mocha,
        "soy": Soy,
        "whip": Whip,
        "caramel": Caramel,
    }
    b = base
    for c in condiments:
        key = c.strip().lower()
        try:
            b = mapping[key](b)
        except KeyError:
            options = ", ".join(sorted(mapping))
            raise ValueError(f"Condimento desconocido: '{c}'. Opciones válidas: {options}")
    return b