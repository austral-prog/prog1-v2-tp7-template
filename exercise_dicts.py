# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    pass  # Reemplazar con tu implementación


def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    pass  # Reemplazar con tu implementación


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    pass  # Reemplazar con tu implementación


def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    pass  # Reemplazar con tu implementación


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    pass  # Reemplazar con tu implementación
