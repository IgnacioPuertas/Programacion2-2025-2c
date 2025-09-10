from .ingredients import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory, PizzaIngredientFactory
from .pizza import Pizza, CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza
from .store import NYPizzaStore, ChicagoPizzaStore

import pytest

def test_ny_pizza_store_creates_ny_style_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert "NY Style" in pizza.name
    assert isinstance(pizza, CheesePizza)

def test_chicago_pizza_store_creates_chicago_style_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert "Chicago Style" in pizza.name
    assert isinstance(pizza,ClamPizza)

def test_ny_cheese_pizza_has_correct_ingredients():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert str(pizza.dough) == "Thin Crust Dough"
    assert str(pizza.sauce) == "Marinara Sauce"
    assert str(pizza.cheese) == "Reggiano Cheese"

def test_chicago_clam_pizza_has_correct_ingredients():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert str(pizza.dough) == "Thick Crust Dough"
    assert str(pizza.sauce) == "Plum Tomato Sauce"
    assert str(pizza.cheese) == "Mozzarella Cheese"
    assert str(pizza.clam) == "Frozen Clams"

def test_pepperoni_and_veggie_pizzas_created_correctly():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    
    ny_pizza = ny_store.order_pizza("pepperoni")
    chicago_pizza = chicago_store.order_pizza("veggie")
    
    assert "NY Style" in ny_pizza.name
    assert str(ny_pizza.pepperoni) == "Sliced Pepperoni"
    
    assert "Chicago Style" in chicago_pizza.name
    veggie_names = [str(v) for v in chicago_pizza.veggies]
    assert "Spinach" in veggie_names
    assert "Eggplant" in veggie_names