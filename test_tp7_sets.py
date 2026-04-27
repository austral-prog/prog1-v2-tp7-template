import unittest
import exercise_sets as ex


class TestCleanIngredients(unittest.TestCase):

    def test_sin_duplicados(self):
        """Receta sin ingredientes duplicados"""
        result = ex.clean_ingredients(
            'Shakshuka',
            ['tomatoes', 'olive oil', 'cumin', 'harissa']
        )
        nombre, ingredientes = result
        self.assertEqual('Shakshuka', nombre)
        self.assertEqual({'tomatoes', 'olive oil', 'cumin', 'harissa'}, ingredientes)

    def test_con_duplicados(self):
        """Receta con varios ingredientes repetidos"""
        result = ex.clean_ingredients(
            'Waakye',
            ['baking soda', 'sorghum stems', 'coconut oil', 'black-eyed peas',
             'water', 'salt', 'white rice', 'baking soda', 'baking soda',
             'sorghum stems', 'sorghum stems', 'sorghum stems', 'coconut oil']
        )
        nombre, ingredientes = result
        self.assertEqual('Waakye', nombre)
        expected = {'baking soda', 'sorghum stems', 'coconut oil',
                    'black-eyed peas', 'water', 'salt', 'white rice'}
        self.assertEqual(expected, ingredientes)

    def test_retorna_tupla(self):
        """Debe retornar una tupla con (nombre, set)"""
        result = ex.clean_ingredients('Test', ['a', 'b', 'a'])
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertIsInstance(result[1], set)

    def test_set_elimina_duplicados(self):
        """El set final debe tener los ingredientes únicos"""
        ingredientes = ['tomato', 'tomato', 'tomato', 'onion', 'onion']
        result = ex.clean_ingredients('Sauce', ingredientes)
        self.assertEqual({'tomato', 'onion'}, result[1])

    def test_lista_vacia(self):
        """Receta sin ingredientes"""
        result = ex.clean_ingredients('Agua', [])
        self.assertEqual(('Agua', set()), result)


class TestCheckDrinks(unittest.TestCase):

    def test_mocktail_simple(self):
        """Bebida sin alcohol es un Mocktail"""
        result = ex.check_drinks(
            'Honeydew Cucumber',
            ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']
        )
        self.assertEqual('Honeydew Cucumber Mocktail', result)

    def test_cocktail_con_scotch(self):
        """Bebida con scotch es un Cocktail"""
        result = ex.check_drinks(
            'Shirley Tonic',
            ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']
        )
        self.assertEqual('Shirley Tonic Cocktail', result)

    def test_cocktail_con_vodka(self):
        """Bebida con vodka es un Cocktail"""
        result = ex.check_drinks(
            'Moscow Mule',
            ['vodka', 'ginger beer', 'lime juice']
        )
        self.assertEqual('Moscow Mule Cocktail', result)

    def test_cocktail_con_gin(self):
        """Bebida con gin es un Cocktail"""
        result = ex.check_drinks(
            'Gin Tonic',
            ['gin', 'tonic water', 'lemon']
        )
        self.assertEqual('Gin Tonic Cocktail', result)

    def test_mocktail_jugo(self):
        """Jugo de frutas es un Mocktail"""
        result = ex.check_drinks(
            'Fruit Punch',
            ['orange juice', 'pineapple juice', 'grenadine', 'soda']
        )
        self.assertEqual('Fruit Punch Mocktail', result)

    def test_cocktail_con_rum(self):
        """Bebida con rum es un Cocktail"""
        result = ex.check_drinks(
            'Mojito',
            ['mint leaves', 'lime', 'sugar', 'rum', 'club soda']
        )
        self.assertEqual('Mojito Cocktail', result)


if __name__ == '__main__':
    unittest.main()
