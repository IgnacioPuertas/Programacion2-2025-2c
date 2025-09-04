# test_builder_and_sizes.py
import pytest
from beverages import Beverage, Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Milk, Mocha, Soy, Whip, Caramel
from builder import build_beverage

# Función auxiliar para comparar floats con tolerancia
def approx(x, tol=1e-9):
    return pytest.approx(x, rel=tol, abs=tol)



# Test para cafés base y tamaños

def test_beverage_sizes_constant_exists_and_values():
    assert isinstance(Beverage.SIZES, tuple)
    assert Beverage.SIZES == ("Tall", "Grande", "Venti")

@pytest.mark.parametrize("cls, precio", [
    (Espresso,   1.99),
    (DarkRoast,  0.99),
    (HouseBlend, 0.89),
    (Decaf,      1.05),
])
def test_base_beverage_prices_and_default_size(cls, precio):
    b = cls()
    assert b.get_description() != ""  # Tiene alguna descripción
    assert b.get_size() == "Tall"     # Tamaño por defecto
    assert b.cost() == approx(precio)

@pytest.mark.parametrize("size", ["Tall", "Grande", "Venti"])
def test_set_size_valid(size):
    b = Espresso()
    b.set_size(size)
    assert b.get_size() == size

def test_set_size_invalid_raises():
    b = Espresso()
    with pytest.raises(ValueError) as e:
        b.set_size("Gigante")
    assert "Tamaño inválido" in str(e.value)



# Test para condimentos (fijos y con tamaño)

@pytest.mark.parametrize("size, soy_extra", [
    ("Tall",   0.10),
    ("Grande", 0.15),
    ("Venti",  0.20),
])
def test_soy_depende_de_tamanio(size, soy_extra):
    base = Espresso(size=size)     # 1.99
    beb  = Soy(base)               # + segun tamaño
    assert beb.get_size() == size  # delega al base
    assert beb.cost() == approx(1.99 + soy_extra)

@pytest.mark.parametrize("decorator_cls, extra_fijo", [
    (Milk,   0.10),
    (Mocha,  0.20),
    (Whip,   0.10),
    (Caramel,0.25),
])
@pytest.mark.parametrize("size", ["Tall", "Grande", "Venti"])
def test_condimentos_fijos_no_depende_tamanio(decorator_cls, extra_fijo, size):
    base = DarkRoast(size=size)    # 0.99
    beb  = decorator_cls(base)
    assert beb.get_size() == size
    assert beb.cost() == approx(0.99 + extra_fijo)



# Test para COMPOSICIONES / ORDEN / MULTIPLES CONDIMENTOS

def test_multiples_condimentos_costos():
    # HouseBlend (0.89) + Soy (Tall=0.10) + Mocha (0.20) + Whip (0.10)
    base = HouseBlend()            # Tall por default
    beb  = Whip(Mocha(Soy(base)))
    assert beb.get_size() == "Tall"
    esperado = 0.89 + 0.10 + 0.20 + 0.10
    assert beb.cost() == approx(esperado)
    assert beb.get_description().startswith("Café de la Casa")

def test_doble_mocha_costo():
    base = DarkRoast()             # 0.99
    beb  = Mocha(Mocha(base))      # +0.20 +0.20
    assert beb.cost() == approx(0.99 + 0.20 + 0.20)

def test_doble_soy_tamanio_sensitive():
    # Espresso Venti (1.99) + Soy(Venti=0.20) + Soy(Venti=0.20)
    base = Espresso()
    base.set_size("Venti")
    beb  = Soy(Soy(base))
    assert beb.get_size() == "Venti"
    assert beb.cost() == approx(1.99 + 0.20 + 0.20)



# Test para BUILDER: mapeo, case-insensitive, orden y errores

def test_build_beverage_case_insensitive_and_order_preserved():
    # Espresso "Grande" con [" soy ", "Mocha", "whip"]
    # 1.99 + Soy(Grande=0.15) + Mocha(0.20) + Whip(0.10)
    beb = build_beverage(Espresso(), "Grande", [" soy ", "Mocha", "whip"])
    assert beb.get_size() == "Grande"
    assert beb.cost() == approx(1.99 + 0.15 + 0.20 + 0.10)
    # Descripción termina con el orden dado
    desc = beb.get_description()
    assert "Soja" in desc and "Mocha" in desc and "Crema" in desc
    # Verificación básica de orden (no estricta, pero razonable)
    assert ", Soja" in desc and ", Mocha" in desc and ", Crema" in desc

def test_build_beverage_unknown_condiment_raises_valueerror():
    with pytest.raises(ValueError) as e:
        build_beverage(HouseBlend(), "Tall", ["soy", "azucar"])
    msg = str(e.value).lower()
    assert "condimento desconocido" in msg
    assert "opciones válidas" in msg

def test_build_beverage_multiple_caramel_and_size_venti():
    # HouseBlend Venti + Caramel + Caramel + Whip
    beb = build_beverage(HouseBlend(), "Venti", ["caramel", "caramel", "whip"])
    esperado = 0.89 + 0.25 + 0.25 + 0.10
    assert beb.cost() == approx(esperado)
    assert beb.get_size() == "Venti"