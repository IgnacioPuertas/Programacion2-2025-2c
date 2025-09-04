## Informe Patron **Decorator** (Starbuzz Coffee)

## Resumen 

El presente informe detalla la implementación y extensión del patrón Decorator aplicado en el sistema Starbuzz Coffee. Se realizaron tres niveles de implementación: incorporación de un nuevo condimento, adaptación de tamaños para bebidas, y mejoras en la usabilidad a través de un builder y pruebas.

El patrón Decorator permite añadir responsabilidades a objetos de forma dinámica sin modificar su estructura, favoreciendo la flexibilidad y evitando el crecimiento excesivo de subclases.

# Nivel 1 — Implementación de un nuevo condimento

Se incorporo una clase `Caramel`, siguiendo el patrón establecido para los condimentos preexistentes.
La implementación se realizó extendiendo la superclase`CondimentDecorator` manteniendo la consistencia estructural con el resto del sistema sin violar el principio **Open - Closed**

Se implementaron los metodos `get_description()` y `cost()` Esta etapa no presento grandes dificultades ya que solo consistio de una extension directa de la superclase

# Nivel 2 — Implementación de tamaños para un condimento en particular (Soy/soja)

En esta etapa se incorporaron nuevos métodos en la superclase `Beverage`:

- `set_size()`: Con validación para asegurar que el tamaño ingresado sea el correcto.
- `get_size()`: Permite consultar y obtener el tamaño de la bebida.

Además se añadió la tupla size con las constantes **TALL/GRANDE/VENTI** dicho valores son constantes porque representan un conjunto fijo de valores del dominio. Esto garantiza la consistencia en todo el sistema, facilita la validación de entradas y mejora la claridad del codigo evitando repeticiones.

El atributo `size` fue incluido en el constructor `__init__`, heredandose a todas las subclases de `Beverage` mediante `super().__init__()`.

Tambien se realizaron cambios en `condimentos.py`:

- `get_size()`: en la super clase `CondimentDecorator` y en la clase `Soy`
- Se modificó el método `cost()` incorporando un diccionario llamado `extra`, donde se define el costo adicional según el tamaño.
- En caso de no declararse un tamaño, se asigna por defecto Tall.

Las dificultades para este nivel fueron relaizar no solo los cambios en `beverage.py` sino tambien entender que `condiments.py` requeria tambien un getter ya que tambien requiere acceder a dicho tamaño. Si `CondimentDecorator` no lo implementa, cuando un condimento (por ejemplo Soy) intente consultar el tamaño de la bebida que envuelve, no tendría cómo hacerlo directamente.

# Nivel 3 Usabilidad y pruebas 

# Implementación del builder

Se implemento una funcion `build_beverage` que recibe:

- Una base (objeto de tipo Beverage).
- Un tamaño.
- Una lista de condimentos.

La función aplica el `set_size` correspondiente y utiliza un mapeo para los condimentos, garantizando coincidencia con los ingredientes mediante el uso de `strip().lower().`

# Pruebas de las implementaciones

Las pruebas se realizaron en dos niveles:

- Pruebas manuales en `main.py`: Se construyeron diferentes combinaciones de bebidas y condimentos para verificar descripciones y costos correctos, asegurando el buen funcionamiento de los decoradores.

- Pruebas automatizadas con `pytest`: Se verificaron costos, tamaños y descripciones de forma individual y sistemática, validando el comportamiento esperado en cada construcción de bebidas.

# Conclusión

Las implementaciones realizadas ampliaron la funcionalidad del sistema Starbuzz Coffee, manteniendo la flexibilidad del patrón Decorator.

Se logró:

- Incorporar un nuevo condimento sin modificar las clases existentes.
- Adaptar tamaños para condimentos específicos.
- Mejorar la usabilidad con un builder.
- Validar el funcionamiento mediante pruebas manuales y automatizadas.