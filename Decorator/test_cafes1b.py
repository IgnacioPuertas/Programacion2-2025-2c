import pytest
from beverages import HouseBlend, Espresso, DarkRoast
from condiments import Mocha, Whip, Soy, Caramel

PRICES = {
    "Espresso": 1.99,
    "DarkRoast": 0.99,
    "HouseBlend": 0.89,
    "Decaf": 1.05,
    "Mocha": 0.20,
    "Whip": 0.10,
    "Soy": 0.15,
    "Caramel": 0.25,
}

def precio_esperado(base, condiments):
    total = PRICES[base]
    for c in condiments:
        total += PRICES[c]
    return total


def test_espresso_simple():
    beverage = Espresso()
    esperado = precio_esperado("Espresso", [])
    assert beverage.cost() == esperado
    assert beverage.get_description() == "Espresso"


def test_darkroast_doble_mocha_whip():
    beverage = DarkRoast()
    beverage = Mocha(beverage)
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    esperado = precio_esperado("DarkRoast", ["Mocha", "Mocha", "Whip"])
    assert pytest.approx(beverage.cost(), 0.001) == esperado
    assert beverage.get_description() == "Café Dark Roast, Mocha, Mocha, Crema"

# Test Nivel 1
# def test_houseblend_soy_mocha_whip():
#     beverage = HouseBlend()
#     beverage = Soy(beverage)
#     beverage = Mocha(beverage)
#     beverage = Whip(beverage)
#     esperado = precio_esperado("HouseBlend", ["Soy", "Mocha", "Whip"])
#     assert pytest.approx(beverage.cost(), 0.001) == esperado
#     assert beverage.get_description() == "Café de la Casa, Soja, Mocha, Crema"


def test_darkroast_caramel():
    beverage = DarkRoast()
    beverage = Caramel(beverage)
    esperado = precio_esperado("DarkRoast", ["Caramel"])
    assert pytest.approx(beverage.cost(), 0.001) == esperado
    assert beverage.get_description() == "Café Dark Roast, Caramelo"


def test_houseblend_doble_caramel_whip():
    beverage = HouseBlend()
    beverage = Caramel(beverage)
    beverage = Caramel(beverage)
    beverage = Whip(beverage)
    esperado = precio_esperado("HouseBlend", ["Caramel", "Caramel", "Whip"])
    assert pytest.approx(beverage.cost(), 0.001) == esperado
    assert beverage.get_description() == "Café de la Casa, Caramelo, Caramelo, Crema"
