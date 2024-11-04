from Interfaz.Ihabitaciones import HotelApp

#Clase GestorInterfaces
def usar_IHabitaciones():
    habitaciones = HotelApp()
    habitaciones.listar_habitaciones()
    # Aquí puedes llamar a los métodos de IHabitaciones
    # Por ejemplo: habitaciones.algun_metodo()
    
class GestorInterfaces:
    def __init__(self):
        pass

    def RegistrarHabitacion(self, habitacion):
        # Código para registrar una habitación
        pass

    def RegistrarCliente(self, cliente):
        # Código para registrar un cliente
        pass

    def RegistrarReserva(self, reserva):
        # Código para registrar una reserva
        pass

    def RegistrarFactura(self, factura):
        # Código para registrar una factura
        pass