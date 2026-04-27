# TP7 - Trabajo Práctico 7

## Temas evaluados

Estructuras de datos en Python: **tuplas**, **sets (conjuntos)** y **diccionarios**. Operaciones, métodos y patrones comunes para cada una.

## Cómo ejecutar los tests

Para verificar todos los ejercicios en el directorio actual:

```bash
python3 -m unittest discover
```

Para verificar un ejercicio en particular:

```bash
python3 -m unittest test_tp7_tuples
```

O ejecutar directamente:

```bash
python3 test_tp7_tuples.py
```

---

## Parte 1 — Tuplas

Azara y Rui son compañeros de equipo en una búsqueda del tesoro pirata.
Uno tiene una lista de tesoros con coordenadas, el otro una lista de ubicaciones con coordenadas.

**Lista de Azara:**

| Tesoro                      | Coordenada |
| --------------------------- | ---------- |
| Amethyst Octopus            | 1F         |
| Angry Monkey Figurine       | 5B         |
| Antique Glass Fishnet Float | 3D         |
| Brass Spyglass              | 4B         |
| Carved Wooden Elephant      | 8C         |

**Lista de Rui:**

| Ubicación                             | Coordenada  | Cuadrante |
| ------------------------------------- | ----------- | --------- |
| Seaside Cottages                      | ("1", "C")  | Blue      |
| Aqua Lagoon (Island of Mystery)       | ("1", "F")  | Yellow    |
| Abandoned Lighthouse                  | ("4", "B")  | Blue      |
| Stormy Breakwater                     | ("5", "B")  | Purple    |
| Foggy Seacave                         | ("8", "C")  | Purple    |

Las coordenadas de Azara y Rui están con formatos distintos. Ayudá a organizarlas.

Los 3 ejercicios de esta parte se resuelven en el mismo archivo: `exercise_tuples.py`.

**Archivo de test:** `test_tp7_tuples.py`

---

### Ejercicio 1 — `get_coordinate`

**Conceptos:** acceso a elementos de una tupla por índice.

**Consigna:** Implementar `get_coordinate(registro)` que recibe una tupla `(tesoro, coordenada)` y devuelve solo la coordenada.

**Ejemplo:** Para `('Scrimshawed Whale Tooth', '2A')` la salida esperada es:

```
'2A'
```

---

### Ejercicio 2 — `convert_coordinate`

**Conceptos:** creación de tuplas, acceso a caracteres de un string.

**Consigna:** Implementar `convert_coordinate(coordenada)` que recibe una coordenada en formato `"2A"` y devuelve una tupla `("2", "A")` con sus componentes.

**Ejemplo:** Para `"2A"` la salida esperada es:

```
('2', 'A')
```

Para `"7F"` la salida esperada es:

```
('7', 'F')
```

---

### Ejercicio 3 — `create_record`

**Conceptos:** combinación de tuplas, reutilización de funciones, comparación.

**Consigna:** Implementar `create_record(registro_azara, registro_rui)` que combine ambos registros si las coordenadas coinciden.

- `registro_azara`: tupla `(tesoro, coordenada)` → ej: `('Brass Spyglass', '4B')`
- `registro_rui`: tupla `(ubicacion, coordenada, cuadrante)` → ej: `('Abandoned Lighthouse', ('4', 'B'), 'Blue')`

Si las coordenadas coinciden, retornar `(tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)`.
Si NO coinciden, retornar el string `"not a match"`.

**Ejemplo:**

```python
create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
# → ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'Blue'))
# → 'not a match'
```

**Tip:** podés reutilizar `get_coordinate` y `convert_coordinate` para normalizar las coordenadas antes de compararlas.

---

## Parte 2 — Sets (Conjuntos)

Operás una pequeña empresa de catering y el club de cocina local te pide ayuda para organizar un evento.

Los 2 ejercicios de esta parte se resuelven en el mismo archivo: `exercise_sets.py`.

**Archivo de test:** `test_tp7_sets.py`

---

### Ejercicio 4 — `clean_ingredients`

**Conceptos:** conversión de lista a `set`, eliminación de duplicados.

**Consigna:** Las recetas fueron agregadas desde varias fuentes y tienen ingredientes duplicados. Implementar `clean_ingredients(nombre_plato, ingredientes)` que retorne una tupla `(nombre_plato, set_de_ingredientes)` sin duplicados.

**Ejemplo:**

```python
clean_ingredients('Punjabi-Style Chole',
                  ['onions', 'tomatoes', 'ginger paste', 'ginger paste',
                   'chickpeas', 'chickpeas'])
# → ('Punjabi-Style Chole',
#    {'onions', 'tomatoes', 'ginger paste', 'chickpeas'})
```

---

### Ejercicio 5 — `check_drinks`

**Conceptos:** operador `in` con sets, iteración, retorno temprano.

**Consigna:** El evento incluye cócteles y mocktails. Implementar `check_drinks(nombre_bebida, ingredientes)` que devuelva:

- `"<nombre> Cocktail"` si algún ingrediente está en el set `ALCOHOLS` (definido al inicio del archivo).
- `"<nombre> Mocktail"` si ningún ingrediente es alcohólico.

**Ejemplo:**

```python
check_drinks('Honeydew Cucumber',
             ['honeydew', 'coconut water', 'mint leaves', 'lime juice'])
# → 'Honeydew Cucumber Mocktail'

check_drinks('Shirley Tonic',
             ['cinnamon stick', 'scotch', 'whole cloves', 'ginger'])
# → 'Shirley Tonic Cocktail'
```

**Tip:** verificar pertenencia con `in` sobre un `set` es eficiente (O(1)).

---

## Parte 3 — Diccionarios

Administrás un sistema de inventario organizado por el nombre del artículo y la cantidad disponible. Las siguientes funciones te permiten crear, agregar, descontar, eliminar y listar ítems.

Los 5 ejercicios de esta parte se resuelven en el mismo archivo: `exercise_dicts.py`.

**Archivo de test:** `test_tp7_dicts.py`

---

### Ejercicio 6 — `create_inventory`

**Conceptos:** creación de diccionarios, conteo de ocurrencias.

**Consigna:** Implementar `create_inventory(items)` que reciba una lista y devuelva un `dict` con cada item y la cantidad de veces que aparece.

**Ejemplo:**

```python
create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
# → {"coal": 1, "wood": 2, "diamond": 3}
```

---

### Ejercicio 7 — `add_items`

**Conceptos:** acceso y modificación de diccionarios, operador `in`.

**Consigna:** Implementar `add_items(inventario, items)` que agregue cada elemento de la lista al inventario. Si el item ya existe, incrementar su cantidad en 1; si no, agregarlo con cantidad 1.

**Ejemplo:**

```python
add_items({"coal": 1}, ["wood", "iron", "coal", "wood"])
# → {"coal": 2, "wood": 2, "iron": 1}
```

---

### Ejercicio 8 — `decrement_items`

**Conceptos:** modificación de diccionarios, validaciones de rango.

**Consigna:** Implementar `decrement_items(inventario, items)` que reste 1 por cada aparición del item en la lista. **Las cantidades no pueden ser negativas**: si un item aparece más veces que su stock, debe quedar en 0 y las solicitudes extra se ignoran.

**Ejemplo:**

```python
decrement_items({"coal": 3, "diamond": 1, "iron": 5},
                ["diamond", "coal", "iron", "iron"])
# → {"coal": 2, "diamond": 0, "iron": 3}

decrement_items({"coal": 2, "wood": 1, "diamond": 2},
                ["coal", "coal", "wood", "wood", "diamond"])
# → {"coal": 0, "wood": 0, "diamond": 1}
```

---

### Ejercicio 9 — `remove_item`

**Conceptos:** eliminación con `del` o `pop`, validación con `in`.

**Consigna:** Implementar `remove_item(inventario, item)` que elimine por completo el item del inventario. Si el item no existe, retornar el inventario sin cambios.

**Ejemplo:**

```python
remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coal")
# → {"wood": 1, "diamond": 2}

remove_item({"coal": 2, "wood": 1, "diamond": 2}, "gold")
# → {"coal": 2, "wood": 1, "diamond": 2}
```

---

### Ejercicio 10 — `list_inventory`

**Conceptos:** método `.items()`, list comprehension, filtrado.

**Consigna:** Implementar `list_inventory(inventario)` que retorne una lista de tuplas `(item, cantidad)` con los items disponibles. **Solo incluir los items con cantidad mayor a 0.**

**Ejemplo:**

```python
list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0})
# → [('coal', 7), ('wood', 11), ('diamond', 2), ('iron', 7)]
```
