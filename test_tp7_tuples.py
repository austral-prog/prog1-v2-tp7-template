import unittest
import exercise_tuples as ex


class TestGetCoordinate(unittest.TestCase):

    def test_coordenada_simple(self):
        """Extraer coordenada de una tupla básica"""
        result = ex.get_coordinate(('Scrimshawed Whale Tooth', '2A'))
        self.assertEqual('2A', result)

    def test_coordenada_con_letra_f(self):
        """Extraer coordenada con columna F"""
        result = ex.get_coordinate(('Pirate Flag', '7F'))
        self.assertEqual('7F', result)

    def test_coordenada_con_numero_alto(self):
        """Extraer coordenada con un número alto"""
        result = ex.get_coordinate(('Model Ship in Large Bottle', '8A'))
        self.assertEqual('8A', result)

    def test_coordenada_1c(self):
        """Extraer coordenada 1C"""
        result = ex.get_coordinate(('Robot Parrot', '1C'))
        self.assertEqual('1C', result)

    def test_coordenada_distinta(self):
        """Extraer coordenada 4E"""
        result = ex.get_coordinate(('Silver Seahorse', '4E'))
        self.assertEqual('4E', result)


class TestConvertCoordinate(unittest.TestCase):

    def test_coordenada_2a(self):
        """Convertir coordenada 2A"""
        result = ex.convert_coordinate('2A')
        self.assertEqual(('2', 'A'), result)

    def test_coordenada_7f(self):
        """Convertir coordenada 7F"""
        result = ex.convert_coordinate('7F')
        self.assertEqual(('7', 'F'), result)

    def test_coordenada_1c(self):
        """Convertir coordenada 1C"""
        result = ex.convert_coordinate('1C')
        self.assertEqual(('1', 'C'), result)

    def test_coordenada_8a(self):
        """Convertir coordenada 8A"""
        result = ex.convert_coordinate('8A')
        self.assertEqual(('8', 'A'), result)

    def test_retorna_tupla(self):
        """El resultado debe ser una tupla, no una lista"""
        result = ex.convert_coordinate('4E')
        self.assertIsInstance(result, tuple)


class TestCreateRecord(unittest.TestCase):

    def test_coincidencia_simple(self):
        """Coordenadas coinciden: 5B"""
        azara = ('Angry Monkey Figurine', '5B')
        rui = ('Stormy Breakwater', ('5', 'B'), 'Purple')
        result = ex.create_record(azara, rui)
        expected = ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple')
        self.assertEqual(expected, result)

    def test_coincidencia_8c(self):
        """Coordenadas coinciden: 8C"""
        azara = ('Carved Wooden Elephant', '8C')
        rui = ('Foggy Seacave', ('8', 'C'), 'Purple')
        result = ex.create_record(azara, rui)
        expected = ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple')
        self.assertEqual(expected, result)

    def test_coincidencia_1f(self):
        """Coordenadas coinciden: 1F"""
        azara = ('Amethyst Octopus', '1F')
        rui = ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')
        result = ex.create_record(azara, rui)
        expected = ('Amethyst Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')
        self.assertEqual(expected, result)

    def test_no_coincide_diferente_numero(self):
        """Las coordenadas no coinciden en el número"""
        azara = ('Amethyst Octopus', '1F')
        rui = ('Seaside Cottages', ('1', 'C'), 'Blue')
        result = ex.create_record(azara, rui)
        self.assertEqual('not a match', result)

    def test_no_coincide_diferente_letra(self):
        """Las coordenadas no coinciden en la letra"""
        azara = ('Angry Monkey Figurine', '5B')
        rui = ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')
        result = ex.create_record(azara, rui)
        self.assertEqual('not a match', result)

    def test_no_coincide_completamente(self):
        """Coordenadas totalmente distintas"""
        azara = ('Brass Spyglass', '4B')
        rui = ('Spiky Rocks', ('3', 'D'), 'Yellow')
        result = ex.create_record(azara, rui)
        self.assertEqual('not a match', result)


if __name__ == '__main__':
    unittest.main()
