from Interfaz.Ihabitaciones import HotelApp
from IHabitaciones import IHabitaciones
from IClientes import IClientes


#Clase GestorInterfaces
def usar_IHabitaciones():
    habitaciones = HotelApp()
    habitaciones.listar_habitaciones()
    #crear gestroBD
    
    

    # Aquí puedes llamar a los métodos de IHabitaciones
    # Por ejemplo: habitaciones.algun_metodo()
    
class GestorInterfaces:
    def __init__(self):
        pass

    def RegistrarHabitacion(self, habitacion):
        #1) Abrir la ventana
        #2) Habitacion habitacion = ventana_registrar_habitacion(self.root, self.db)
        #3) Validar X
        #4) GestorBD.registrar_habitacion(habitacion)
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