import pytest
from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel

def test_espresso_simple():
    beverage = Espresso()
    assert beverage.cost() == 1.99
    assert beverage.get_description() == "Espresso"

def test_darkroast_doble_mocha_whip():
    beverage = DarkRoast()
    beverage = Mocha(beverage)
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    assert pytest.approx(beverage.cost(), 0.001) == 1.49
    assert beverage.get_description() == "Café Dark Roast, Mocha, Mocha, Crema"

def test_houseblend_soy_mocha_whip():
    beverage = HouseBlend()
    beverage = Soy(beverage)
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    assert pytest.approx(beverage.cost(), 0.001) == 1.34
    assert beverage.get_description() == "Café de la Casa, Soja, Mocha, Crema"

def test_darkroast_caramel():
    beverage = DarkRoast()
    beverage = Caramel(beverage)
    assert pytest.approx(beverage.cost(), 0.001) == 1.24
    assert beverage.get_description() == "Café Dark Roast, Caramelo"

def test_houseblend_doble_caramel_whip():
    beverage = HouseBlend()
    beverage = Caramel(beverage)
    beverage = Caramel(beverage)
    beverage = Whip(beverage)
    assert pytest.approx(beverage.cost(), 0.001) == 1.49
    assert beverage.get_description() == "Café de la Casa, Caramelo, Caramelo, Crema"
