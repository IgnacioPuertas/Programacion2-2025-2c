from factory.factory_method.store import NYPizzaStore, ChicagoPizzaStore
from factory.factory_method.pizza import NYStyleVeggiePizza, ChicagoStylePepperoniPizza

def test_ny_veggie_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("veggie")
    assert isinstance(pizza, NYStyleVeggiePizza)
    assert "Veggie" in str(pizza)

def test_chicago_pepperoni_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("pepperoni")
    assert isinstance(pizza, ChicagoStylePepperoniPizza)
    assert "Pepperoni" in str(pizza)
