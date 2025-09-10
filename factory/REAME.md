# Trabajo Práctico: Patrones de Diseño Factory

Este repositorio implementa el sistema de **PizzaStore** de Objectville, utilizando los patrones de diseño **Simple Factory**, **Factory Method** y **Abstract Factory**.  
Cada módulo representa una evolución en el diseño para mejorar la **flexibilidad**, **mantenibilidad** y **desacoplamiento** del código.

## Estructura del Repositorio

```
factory/
├── simple_factory/
│ ├── main.py
│ ├── pizza.py
│ ├── simple_factory.py
│ └── store.py
│
├── factory_method/
│ ├── main.py
│ ├── pizza.py
│ ├── store.py
│ └── test_factory_method.py
│
├── abstract_factory/
│ ├── ingredients.py
│ ├── main.py
│ ├── pizza.py
│ ├── store.py
│ └── test_abstract_factory.py
│
├── img/
│ ├── SimpleFactory_diagrama.png
│ ├── Factory_diagrama.png
│ └── Abstract_Factory_diagrama.png
```

## Cómo ejecutar

### 1. Requisitos
- Python 3.11+
- Instalar dependencias:

```bash
pip install -r requirements.txt
```
El archivo requirements.txt contiene únicamente pytest, ya que el código no depende de librerías externas.

### 2. Ejecutar cada patrón

Para ejecutar cada patrón de diseño, navegá a la carpeta correspondiente y ejecutá el archivo main.py. Por ejemplo:

```bash
# Simple Factory
python -m factory.simple_factory.main

# Factory Method
python -m factory.factory_method.main

# Abstract Factory
python -m factory.abstract_factory.main
```

Repití este proceso para cada patrón de diseño.

### 3. Ejecutar pruebas

Para validar el sistema desde el repositorio raíz:

```bash
pytest -q
```
Las pruebas verifican que:

- `NYPizzaStore` y `ChicagoPizzaStore` crean instancias de sus estilos correspondientes.
- Los ingredientes de cada pizza son los correctos según la región.
- Las nuevas variedades (`VeggiePizza`, `PepperoniPizza`) se producen correctamente.

## Diagramas UML

En la carpeta raíz del directorio se encuentran los diagramas de clases de cada patrón:

- Simple Factory → SimpleFactory_diagrama.png

- Factory Method → Factory_diagrama.png

- Abstract Factory → Abstract_Factory_diagrama.png **ver nota de diseño abajo**


## Decisiones de Diseño

### Simple Factory

- Encapsula la creación en SimplePizzaFactory
- No es un patrón GoF formal, pero es un paso hacia Factory Method

### Factory Method

- Delegamos la creación en subclases (`NYPizzaStore`, `ChicagoPizzaStore`)
- Se agregaron `VeggiePizza` y `PepperoniPizza` siguiendo el estilo regional
- En Chicago, algunas pizzas redefinen `cut()` para cortes cuadrados

### Abstract Factory

- Se agregó una jerarquía para manejar familias de ingredientes por región
- Se crearon `Veggies` y `Pepperoni` como clases concretas simples (no se implementaron interfaces de ingredientes para mantener consistencia con el código dado)
- Las pizzas (`Cheese`, `Clam`, `Veggie`, `Pepperoni`) usan una `PizzaIngredientFactory` para obtener ingredientes
- Esta variante asegura consistencia regional: ej. NY siempre usa `Thin Crust Dough`, Chicago siempre `Frozen Clams`


## Notas de diseño

- En **Abstract Factory** no modelamos interfaces de ingredientes; usamos clases concretas y la variación por región está encapsulada en `PizzaIngredientFactory`
- Si una pizza se instancia sin pasar por `order_pizza`, los atributos de ingredientes pueden estar vacíos hasta que se ejecute `prepare()`


## Conclusiones

- Simple Factory resuelve el problema inicial, pero sigue centralizando la lógica de instanciación.
- Factory Method mejora la extensibilidad al delegar la creación a subclases.
- Abstract Factory es la solución más robusta: permite variar familias de productos relacionados (ingredientes) sin modificar el código cliente.

Con los tres enfoques, queda claro el impacto positivo de los patrones de diseño en desacoplar, extender y mantener sistemas en crecimiento.