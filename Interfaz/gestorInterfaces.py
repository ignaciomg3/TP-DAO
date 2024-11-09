from Interfaz.Ihabitacion import ventana_registrar_habitacion
from Interfaz.Imostrar_habitaciones import ventana_ver_habitaciones
from Interfaz.Iclientes import ventana_registrar_cliente, ventana_ver_clientes
from Interfaz.Ireserva import ventana_registrar_reserva
from Interfaz.Iempleados import ventana_registrar_empleado, ventana_ver_empleados
from Interfaz.Ireportes import ventana_reportes
from Interfaz.ventanaPrincipal import HotelApp
from Datos.gestor_db import GestorDB
from tkinter import messagebox
from Entidades.habitacion import Habitacion
from Entidades.reserva import Reserva
from Entidades.empleado import Empleado
from Entidades.cliente import Cliente
from tkcalendar import DateEntry


#Clase GestorInterfaces
def usar_IHabitaciones():
    habitaciones = HotelApp()
    habitaciones.listar_habitaciones()
    #crear gestroBD
    
    

    # Aquí puedes llamar a los métodos de IHabitaciones
    # Por ejemplo: habitaciones.algun_metodo()
    
class GestorInterfaces:
    def __init__(self, root):
        self.root = root
        self.db = GestorDB()
        self.db.borrar_base_de_datos()
        self.db.crear_tablas()

    def RegistrarHabitacion(self, habitacion):
        #1) Abrir la ventana
        #2) Habitacion habitacion = ventana_registrar_habitacion(self.root, self.db)
        #3) Validar X
        #4) GestorBD.registrar_habitacion(habitacion)
        pass

    def abrir_ventana_ver_habitaciones(self):
        ventana_ver_habitaciones(self.root, self.db)

    def abrir_ventana_registrar_cliente(self):
        ventana_registrar_cliente(self.root, self.db)

    def abrir_ventana_ver_clientes(self):
        ventana_ver_clientes(self.root, self.db)

    def abrir_ventana_registrar_reserva(self):
        ventana_registrar_reserva(self.root, self.db)

    def abrir_ventana_registrar_empleado(self):
        ventana_registrar_empleado(self.root, self.db)

    def abrir_ventana_ver_empleados(self):
        ventana_ver_empleados(self.root, self.db)

    def abrir_ventana_reportes(self):
        ventana_reportes(self.root, self.db)

    def registrar_habitacion(self, numero, tipo, estado, precio, ventana):
        if not all([numero, tipo, estado, precio]):
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos antes de registrar.")
            return
        try:
            numero = int(numero)
            precio = float(precio)
            habit = Habitacion(numero, tipo, estado, precio)
            self.db.insertar_habitacion(habit.numero, habit.tipo, habit.estado, habit.precio_por_noche)
            messagebox.showinfo("Registro Exitoso", f"Habitación {numero} registrada con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")

    def registrar_cliente(self, id_cliente, nombre, apellido, direccion, telefono, email, ventana):
        if not all([id_cliente, nombre, apellido, direccion, telefono, email]):
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos antes de registrar.")
            return
        try:
            self.db.insertar_cliente(id_cliente, nombre, apellido, direccion, telefono, email)
            messagebox.showinfo("Registro Exitoso", f"Cliente {nombre} {apellido} registrado con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")

    def registrar_reserva(self, id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas, ventana):
        try:
            if not all([id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas]):
                raise ValueError("Todos los campos son obligatorios.")
            self.db.insertar_reserva(1, id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas)
            consulta = "UPDATE habitaciones SET estado = 'ocupado' WHERE numero = ?"
            parametros = (id_habitacion, )
            self.db.ejecutar_consulta(consulta, parametros)
            messagebox.showinfo("Registro Exitoso", "Reserva registrada con éxito.")
            ventana.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar la reserva: {e}")

    def registrar_empleado(self, id_empleado, nombre, apellido, cargo, sueldo, ventana):
        if not id_empleado or not nombre or not apellido or not cargo or not sueldo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        try:
            self.db.insertar_empleado(id_empleado, nombre, apellido, cargo, sueldo)
            messagebox.showinfo("Registro Exitoso", f"Empleado {nombre} {apellido} registrado con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")