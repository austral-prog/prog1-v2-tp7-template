# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).

    Args:
        registro: Una tupla con el formato (tesoro, coordenada)

    Returns:
        Un string con la coordenada del mapa
    """
    pass  # Reemplazar con tu implementación


def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").

    Args:
        coordenada: Un string con la coordenada (ej: "2A", "7F")

    Returns:
        Una tupla con los componentes individuales (ej: ("2", "A"))
    """
    pass  # Reemplazar con tu implementación


def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.

    - Registro de Azara: (tesoro, coordenada) -> ej: ('Brass Spyglass', '4B')
    - Registro de Rui: (ubicacion, coordenada, cuadrante) ->
      ej: ('Abandoned Lighthouse', ('4', 'B'), 'Blue')

    Si las coordenadas coinciden, retornar una tupla combinada:
    (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)

    Si NO coinciden, retornar el string "not a match".

    Args:
        registro_azara: Tupla (tesoro, coordenada)
        registro_rui: Tupla (ubicacion, coordenada, cuadrante)

    Returns:
        Tupla combinada si las coordenadas coinciden, o "not a match" si no.
    """
    pass  # Reemplazar con tu implementación
