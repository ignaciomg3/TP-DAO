
class Habitacion:
    def __init__(self, numero, tipo, estado, precio_por_noche):
        self.numero = numero
        self.tipo = tipo  # Puede ser 'simple', 'doble' o 'suite'
        self.estado = estado  # 'disponible' o 'ocupada'
        self.precio_por_noche = precio_por_noche
