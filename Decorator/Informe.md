# Informe Patrón **Decorator** — Starbuzz Coffee

## Resumen 

El presente informe detalla la implementación y extensión del patrón Decorator aplicado en el sistema Starbuzz Coffee. Se realizaron tres niveles de implementación: incorporación de un nuevo condimento, adaptación de tamaños para un condimento en particular, y mejoras en la usabilidad a través de un builder y pruebas.

El patrón Decorator permite añadir responsabilidades a objetos de forma dinámica sin modificar su estructura, favoreciendo la flexibilidad y evitando el crecimiento excesivo de subclases. De esta forma se cumple con el principio **Open - Closed**: las clases permanecen abiertas a extensión pero cerradas a modificación.

## Nivel 1 — Implementación de un nuevo condimento

Se incorporó una clase `Caramel`, siguiendo el mismo esquema establecido para los condimentos preexistentes.
La implementación se realizó extendiendo `CondimentDecorator` y redefiniendo los métodos `get_description()` y `cost()`.

Esta etapa no presentó dificultades ya que consistió en una extensión directa de la superclase, manteniendo la consistencia estructural y sin violar el principio **Open - Closed**.

## Nivel 2 — Implementación de tamaños (en Soy)

En esta etapa se incorporaron nuevos métodos en la superclase `Beverage`:

- Se definió el atributo `_size` y la constante `SIZES = ("Tall", "Grande", "Venti")`
- `set_size()`: Con validación para asegurar que el tamaño ingresado sea el correcto.
- `get_size()`: Permite consultar y obtener el tamaño de la bebida.

El atributo `size` fue incluido en el constructor `__init__`, heredándose a todas las subclases de `Beverage` mediante `super().__init__()`.

También se realizaron cambios en `condimentos.py`:

`get_size()`: en la superclase `CondimentDecorator` y en la clase `Soy`
En el condimento `Soy` se redefinió `cost()` con un diccionario que asigna costo adicional según tamaño:

- Tall → +0.10
- Grande → +0.15
- Venti → +0.20

Si no se define un tamaño válido, el valor por defecto es el de Tall.

Las dificultades para este nivel fueron entender que no solo los cambios en `beverage.py` eran suficientes, sino también que `condiments.py` requería de un getter para acceder a dicho tamaño. Sin este getter en `CondimentDecorator`, un condimento como `Soy` no podría calcular el costo adicional en función del tamaño de la bebida base.

## Nivel 3 — Usabilidad y pruebas 

### Implementación del builder

Se implementó una función `build_beverage(base, size, condiments)` que:

- Configura el tamaño en la bebida base,
- Normaliza los nombres de condimentos `(strip().lower())`,
- Aplica un mapeo `string → clase decoradora`,
- Lanza un error claro en caso de condimento desconocido.

De esta manera conseguimos una mejor usabilidad, permitiendo construir bebidas complejas de manera declarativa.

### Pruebas de las implementaciones

Las pruebas se realizaron en dos niveles:

- Pruebas manuales en `main.py`: Se construyeron diferentes combinaciones de bebidas y condimentos para verificar descripciones y costos correctos, asegurando el buen funcionamiento de los decoradores.

- Pruebas automatizadas con `pytest` para validar:
  - precios base y tamaño por defecto,
  - cálculo del extra en Soy según tamaño,
  - condimentos de costo fijo independientes del tamaño,
  - composiciones con múltiples decoradores,
  - comportamiento del builder ante entradas válidas e inválidas.

## Conclusiones

Se logró:

- Incorporar un nuevo condimento sin modificar las clases existentes.
- Incorporar tamaños para condimentos específicos.
- Mejorar la usabilidad con un builder.
- Validar el funcionamiento mediante pruebas manuales y automatizadas.

En conclusión, las implementaciones realizadas ampliaron la funcionalidad del sistema Starbuzz Coffee, manteniendo la flexibilidad del patrón Decorator.
