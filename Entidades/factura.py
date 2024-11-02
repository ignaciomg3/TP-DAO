class Factura:
    def __init__(self, id_factura, cliente, reserva, fecha_emision, total):
        self.id_factura = id_factura
        self.cliente = cliente  # Debe ser una instancia de Cliente
        self.reserva = reserva  # Debe ser una instancia de Reserva
        self.fecha_emision = fecha_emision
        self.total = total
