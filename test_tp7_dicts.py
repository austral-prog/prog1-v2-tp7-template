import unittest
import exercise_dicts as ex


class TestCreateInventory(unittest.TestCase):

    def test_inventario_basico(self):
        """Inventario desde lista con varios items repetidos"""
        result = ex.create_inventory(["wood", "iron", "iron", "diamond", "diamond"])
        self.assertEqual({"wood": 1, "iron": 2, "diamond": 2}, result)

    def test_inventario_vacio(self):
        """Lista vacía genera inventario vacío"""
        result = ex.create_inventory([])
        self.assertEqual({}, result)

    def test_un_solo_item(self):
        """Un solo item en la lista"""
        result = ex.create_inventory(["gold"])
        self.assertEqual({"gold": 1}, result)

    def test_todos_distintos(self):
        """Todos los items son distintos"""
        result = ex.create_inventory(["coal", "iron", "gold", "diamond"])
        self.assertEqual({"coal": 1, "iron": 1, "gold": 1, "diamond": 1}, result)

    def test_mismo_item_varias_veces(self):
        """Un mismo item aparece varias veces"""
        result = ex.create_inventory(["coal", "coal", "coal", "coal"])
        self.assertEqual({"coal": 4}, result)

    def test_ejemplo_consigna(self):
        """Ejemplo de la consigna"""
        result = ex.create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
        self.assertEqual({"coal": 1, "wood": 2, "diamond": 3}, result)


class TestAddItems(unittest.TestCase):

    def test_agregar_items_existentes(self):
        """Incrementar items ya existentes en el inventario"""
        result = ex.add_items({"wood": 4, "iron": 2}, ["iron", "iron"])
        self.assertEqual({"wood": 4, "iron": 4}, result)

    def test_agregar_items_nuevos(self):
        """Agregar items que no existen previamente"""
        result = ex.add_items({"iron": 1, "diamond": 2}, ["iron", "wood", "wood"])
        self.assertEqual({"iron": 2, "diamond": 2, "wood": 2}, result)

    def test_inventario_vacio(self):
        """Agregar items a un inventario vacío"""
        result = ex.add_items({}, ["iron", "iron", "diamond"])
        self.assertEqual({"iron": 2, "diamond": 1}, result)

    def test_lista_vacia(self):
        """Agregar una lista vacía no cambia el inventario"""
        result = ex.add_items({"coal": 3, "iron": 2}, [])
        self.assertEqual({"coal": 3, "iron": 2}, result)

    def test_mezcla_existentes_y_nuevos(self):
        """Mezcla de items existentes y nuevos"""
        result = ex.add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"])
        self.assertEqual({"wood": 3, "gold": 3, "diamond": 3}, result)

    def test_ejemplo_consigna(self):
        """Ejemplo de la consigna"""
        result = ex.add_items({"coal": 1}, ["wood", "iron", "coal", "wood"])
        self.assertEqual({"coal": 2, "wood": 2, "iron": 1}, result)


class TestDecrementItems(unittest.TestCase):

    def test_decrementar_simple(self):
        """Decrementar items del inventario"""
        result = ex.decrement_items(
            {"iron": 3, "diamond": 4, "gold": 2},
            ["iron", "iron", "diamond", "gold", "gold"]
        )
        self.assertEqual({"iron": 1, "diamond": 3, "gold": 0}, result)

    def test_no_baja_de_cero(self):
        """Las cantidades no pueden quedar por debajo de 0"""
        result = ex.decrement_items(
            {"wood": 2, "iron": 3, "diamond": 1},
            ["wood", "wood", "wood", "iron", "diamond", "diamond"]
        )
        self.assertEqual({"wood": 0, "iron": 2, "diamond": 0}, result)

    def test_item_no_existente(self):
        """Decrementar un item que no existe en el inventario"""
        result = ex.decrement_items(
            {"iron": 2},
            ["iron", "gold"]
        )
        self.assertEqual({"iron": 1}, result)

    def test_lista_vacia(self):
        """Lista vacía no modifica el inventario"""
        result = ex.decrement_items({"coal": 3, "iron": 2}, [])
        self.assertEqual({"coal": 3, "iron": 2}, result)

    def test_ejemplo_consigna(self):
        """Ejemplo de la consigna"""
        result = ex.decrement_items(
            {"coal": 3, "diamond": 1, "iron": 5},
            ["diamond", "coal", "iron", "iron"]
        )
        self.assertEqual({"coal": 2, "diamond": 0, "iron": 3}, result)

    def test_ejemplo_no_negativos(self):
        """Ejemplo de la consigna sobre no negativos"""
        result = ex.decrement_items(
            {"coal": 2, "wood": 1, "diamond": 2},
            ["coal", "coal", "wood", "wood", "diamond"]
        )
        self.assertEqual({"coal": 0, "wood": 0, "diamond": 1}, result)


class TestRemoveItem(unittest.TestCase):

    def test_remover_item_existente(self):
        """Remover un item que existe en el inventario"""
        result = ex.remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond")
        self.assertEqual({"iron": 1, "gold": 1}, result)

    def test_remover_item_inexistente(self):
        """Remover un item que NO existe retorna el inventario sin cambios"""
        result = ex.remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood")
        self.assertEqual({"iron": 1, "diamond": 2, "gold": 1}, result)

    def test_remover_de_inventario_vacio(self):
        """Remover de un inventario vacío retorna vacío"""
        result = ex.remove_item({}, "gold")
        self.assertEqual({}, result)

    def test_remover_unico_item(self):
        """Remover el único item del inventario"""
        result = ex.remove_item({"coal": 5}, "coal")
        self.assertEqual({}, result)

    def test_ejemplo_consigna(self):
        """Ejemplo de la consigna"""
        result = ex.remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coal")
        self.assertEqual({"wood": 1, "diamond": 2}, result)

    def test_ejemplo_item_no_existe(self):
        """Ejemplo de la consigna con item que no existe"""
        result = ex.remove_item({"coal": 2, "wood": 1, "diamond": 2}, "gold")
        self.assertEqual({"coal": 2, "wood": 1, "diamond": 2}, result)


class TestListInventory(unittest.TestCase):

    def test_lista_basica(self):
        """Listar inventario con items válidos"""
        result = ex.list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0})
        self.assertEqual(
            sorted([("coal", 15), ("diamond", 3), ("wood", 67)]),
            sorted(result)
        )

    def test_excluye_ceros(self):
        """Items con cantidad 0 no deben incluirse"""
        result = ex.list_inventory({"coal": 0, "iron": 5, "gold": 0})
        self.assertEqual([("iron", 5)], result)

    def test_inventario_vacio(self):
        """Inventario vacío retorna lista vacía"""
        result = ex.list_inventory({})
        self.assertEqual([], result)

    def test_todos_en_cero(self):
        """Todos los items están en 0 -> lista vacía"""
        result = ex.list_inventory({"coal": 0, "iron": 0})
        self.assertEqual([], result)

    def test_ejemplo_consigna(self):
        """Ejemplo de la consigna"""
        result = ex.list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0})
        expected = [("coal", 7), ("diamond", 2), ("iron", 7), ("wood", 11)]
        self.assertEqual(sorted(expected), sorted(result))

    def test_retorna_lista_de_tuplas(self):
        """El resultado debe ser una lista de tuplas"""
        result = ex.list_inventory({"coal": 1})
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(x, tuple) for x in result))


if __name__ == '__main__':
    unittest.main()
