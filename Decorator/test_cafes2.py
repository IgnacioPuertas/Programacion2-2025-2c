# test_sizes.py
import pytest
from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Soy, Mocha, Whip, Caramel

# Tolerancia para comparaciones de punto flotante
def approx(x, tol=1e-9):
    return pytest.approx(x, rel=tol, abs=tol)

# Pruebas de Soy según tamaño (El resto de los condimentos no varían con el tamaño -fallarían las pruebas si se cambian-)
@pytest.mark.parametrize("size, extra_esperado", [
    ("Tall",   0.10),
    ("Grande", 0.15),
    ("Venti",  0.20),
])

def test_soy_extra_depende_de_tamano(size, extra_esperado):
    base = Espresso(size=size)         # Espresso = 1.99
    bebida = Soy(base)                 # + Soy segun tamaño
    assert bebida.get_size() == size
    assert bebida.cost() == approx(1.99 + extra_esperado)

# Delegación de get_size a través de cadena de decoradores
def test_delegacion_tamano_en_cadena_decoradores():
    base = HouseBlend(size="Venti")    # 0.89
    bebida = Soy(base)                 # +0.20 por Venti
    bebida = Mocha(bebida)             # +0.20
    bebida = Whip(bebida)              # +0.10

    assert bebida.get_size() == "Venti"
    esperado = 0.89 + 0.20 + 0.20 + 0.10
    assert bebida.cost() == approx(esperado)

# PARA PREGUNTAR, ¿qué pasa si llamamos a set_size en el objeto decorado?
# ¿Se propaga el cambio al objeto base?
# ¿Deberíamos implementar set_size en el decorador abstracto para que lo propague?
# ¿Las cafeterías suelen permitir cambiar el tamaño luego de los agregados? ¿O suelen hacerlo solo al principio?
def test_set_size_sobre_objeto_decorado_delega_correctamente():
    base = DarkRoast()                 # por defecto Tall: 0.99
    bebida = Soy(base)                 # +0.10 (Tall)
    assert bebida.get_size() == "Tall"
    assert bebida.cost() == approx(0.99 + 0.10)

    # Ahora cambiamos el tamaño llamando al OBJETO DECORADO
    bebida.set_size("Venti")
    assert bebida.get_size() == "Venti"
    assert bebida.cost() == approx(0.99 + 0.20)

# Pedido 6
def test_pedido_6_espresso_venti_soy_mocha_whip():
    bebida = Espresso()                # 1.99
    bebida.set_size("Venti")           # Venti
    bebida = Soy(bebida)               # +0.20
    bebida = Mocha(bebida)             # +0.20
    bebida = Whip(bebida)              # +0.10
    esperado = 1.99 + 0.20 + 0.20 + 0.10
    assert bebida.cost() == approx(esperado)

# Pedido 7
def test_pedido_7_houseblend_grande_soy_caramel_mocha_whip():
    bebida = HouseBlend()              # 0.89
    bebida.set_size("Grande")          # Grande
    bebida = Soy(bebida)               # +0.15
    bebida = Caramel(bebida)           # +0.25 (fijo)
    bebida = Mocha(bebida)             # +0.20 (fijo)
    bebida = Whip(bebida)              # +0.10 (fijo)
    esperado = 0.89 + 0.15 + 0.25 + 0.20 + 0.10
    assert bebida.cost() == approx(esperado)

# Pedido 8
def test_pedido_8_darkroast_venti_soy_doble_mocha_caramel_whip():
    bebida = DarkRoast()               # 0.99
    bebida.set_size("Venti")           # Venti
    bebida = Soy(bebida)               # +0.20
    bebida = Mocha(bebida)             # +0.20
    bebida = Mocha(bebida)             # +0.20
    bebida = Caramel(bebida)           # +0.25
    bebida = Whip(bebida)              # +0.10
    esperado = 0.99 + 0.20 + 0.20 + 0.20 + 0.25 + 0.10
    assert bebida.cost() == approx(esperado)
