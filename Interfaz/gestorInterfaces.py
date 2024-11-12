#************************ IMPORTS ************************

from Datos.gestor_db import GestorDB

# Importar las clases de las INTERFACES
from Interfaz import Ireportes
from Interfaz.Iclientes import ventana_registrar_cliente, ventana_ver_clientes
from Interfaz.Iempleados import *
from Interfaz.Ihabitacion import *
from Interfaz.Ireserva import *
from Interfaz.Ireportes import *
from Interfaz.ventanaPrincipal import *
from Interfaz.Imostrar_habitaciones import *
from Interfaz.Iasignar_empleado import ventana_asignar_empleado  # Importar la nueva interfaz
#from Interfaz import IReportes2
#from Interfaz.IReportes2 import ventana_reportes  # Importar la nueva interfaz

# Importar clase de ENTIDADES
from Entidades.habitacion import *
from Entidades.cliente import *
from Entidades.empleado import *
from Entidades.reserva import *
from Entidades.factura import *

# Importar librerías necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

import matplotlib.pyplot as plt
from datetime import datetime, date
from time import sleep

# Clase GestorInterfaces
class GestorInterfaces:
    def __init__(self, root, db_parametro, gestor_reportes):
        self.root = root  # Aquí root es una instancia de tk.Tk
        self.db = db_parametro
        self.db.borrar_datos_de_tablas()  # Borrar los DATOS de las tablas en la base de datos
        self.db._insertar_datos_iniciales()  # Insertar datos de prueba en la base de datos
        self.hotel_app = None  # Mantener una referencia a HotelApp
        self.gestor_reportes = gestor_reportes

    def abrir_Ventana_Principal(self):
        print("Abriendo ventana principal por gestorInterfaces")
        self.hotel_app = HotelApp(self.root, self)
        self.hotel_app.mostrarPantalla()

    #***************** HABITACIONES *****************
    def abrir_ventana_registrar_habitacion(self):
        print("Abriendo ventana registrar habitacion")
        habit = ventana_registrar_habitacion(self, self.root)  # Llamar a la interfaz de registro de habitación
        if habit:  # Si la habitación fue creada correctamente, se registra en la base de datos
            self.db.insertar_habitacion(habit.numero, habit.tipo, habit.estado, habit.precio_por_noche)
            messagebox.showinfo("Registro Exitoso", f"Habitación {habit.numero} registrada con éxito.")
        else:
            print("No se registró ninguna habitación.")

    def abrir_ventana_ver_habitaciones(self):
        ventana_ver_habitaciones(self.root, self)
    
    def filtrar_habitaciones(self, fecha_seleccionada):
        return self.db.filtrar_habitaciones(fecha_seleccionada)

    #***************** CLIENTES *****************
    def abrir_ventana_registrar_cliente(self):
        ventana_registrar_cliente(self.root, self.db, self)

    def abrir_ventana_ver_clientes(self):
        clientes = self.db.obtener_clientes()
        ventana_ver_clientes(self.root, clientes)

    #***************** RESERVAS *****************
    def registrar_reserva(self, id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas, ventana):
        try:
            if not all([id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas]):
                raise ValueError("Todos los campos son obligatorios.")
            id_reserva = self.db.obtener_proximo_id_reserva()  # Obtener el próximo ID de reserva
            print(f"tipo de dato del atributo id_reserva: {type(id_reserva)},\n"
                f"tipo de dato del atributo id_cliente: {type(id_cliente)},\n"
                f"tipo de dato del atributo id_habitacion: {type(id_habitacion)},\n"
                f"tipo de dato del atributo fecha_inicio: {type(fecha_inicio)},\n"
                f"tipo de dato del atributo fecha_fin: {type(fecha_fin)},\n"
                f"tipo de dato del atributo cant_personas: {type(cant_personas)}")
            #messagebox.showinfo("id de la última reserva:",id_reserva)
            #mostrar el tipo de dato del id_reserva
            print(type(id_reserva))
            id_reserva = int(id_reserva)
            self.db.insertar_reserva(id_reserva, id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas)
            consulta = "UPDATE habitaciones SET estado = 'ocupada' WHERE numero = ?"
            parametros = (id_habitacion,)
            self.db.ejecutar_consulta(consulta, parametros)
            messagebox.showinfo("Registro Exitoso", "Reserva registrada con éxito.")
            # mostrar la reserva, la habitación 
            reserva = self.db.obtener_reserva(id_reserva)
            #messagebox.showinfo("Reserva Registrada", f"Reserva ID: {reserva[0]}\nCliente ID: {reserva[1]}\nHabitación ID: {reserva[2]}\nFecha Inicio: {reserva[3]}\nFecha Fin: {reserva[4]}\nCantidad de Personas: {reserva[5]}")
           
            # Generar factura de la reserva
            # Obtener los detalles de la habitación a partir de su ID
            habitacion = self.db.obtener_habitacion(id_habitacion)
            # Extraer el precio por noche de la habitación
            precio_por_noche = habitacion[3]
            
            # Convertir las fechas de inicio y fin de string a objeto date si es necesario
            if isinstance(fecha_inicio, str) and fecha_inicio:
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            if isinstance(fecha_fin, str) and fecha_fin:
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                
            # Calcular el número de días de la reserva
            if fecha_inicio and fecha_fin:
                dias = (fecha_fin - fecha_inicio).days
            else:
                dias = 0
            total_reserva = precio_por_noche * dias
            
            proximo_id_factura = self.db.obtener_proximo_id_factura()

            #LLamar a una función que se encargue de generar la factura
            self.db.insertar_factura(proximo_id_factura, id_cliente, id_reserva, fecha_fin, total_reserva )
            print("Factura generada con éxito")

            #self.db.insertar_factura_autoincremental(id_cliente, id_reserva, fecha_fin, total_reserva)
            #print("Factura autoincremental generada con éxito")
            
            ventana.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar la reserva: {e}")
    
    def abrir_ventana_registrar_reserva(self):
        ventana_registrar_reserva(self.root, self)

    

    #***************** EMPLEADOS *****************
    def abrir_ventana_registrar_empleado(self):
        ventana_registrar_empleado(self.root, self.db, self)

    def abrir_ventana_ver_empleados(self):
        empleados = self.db.obtener_empleados()
        ventana_ver_empleados(self.root, empleados)

    # ***************** REPORTES *****************
    def abrir_ventana_reportes(self):
        # GestorI -> IReportes 
        ventana_reportes(self.root, self.db)

    def abrir_ventana_asignar_empleado(self):
        empleados_limpieza = [Empleado(*e) for e in self.db.obtener_empleados_por_cargo("Servicio de limpieza")]
        ventana_asignar_empleado(self.root, self, empleados_limpieza)

    def registrar_servicio_limpieza(self, id_empleado, id_habitacion, fecha, ventana):
        if not all([id_empleado, id_habitacion, fecha]):
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos antes de registrar.")
            return
        try:
            self.db._crear_tabla_servicio_limpieza()  # Asegurarse de que la tabla exista
            self.db.insertar_servicio_limpieza(id_empleado, id_habitacion, fecha)
            messagebox.showinfo("Registro Exitoso", "Servicio de limpieza registrado con éxito.")
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar el servicio de limpieza: {e}")

    def registrar_habitacion(self, numero, tipo, estado, precio, ventana):
        # Validaciones previas
        if not all([numero, tipo, estado, precio]):
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos antes de registrar.")
            return
        try:
            # Creación del objeto Habitacion
            numero = int(numero)
            precio = float(precio)
            habit = Habitacion(numero, tipo, estado, precio)

            # Registrar la habitación en la base de datos
            self.db.insertar_habitacion(habit.numero, habit.tipo, habit.estado, habit.precio_por_noche)
            messagebox.showinfo("Registro Exitoso", f"Habitación {numero} registrada con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")

    def registrar_cliente(self, nombre, apellido, direccion, telefono, email, ventana):
        if not all([nombre, apellido, direccion, telefono, email]):
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos antes de registrar.")
            return
        try:
            id_cliente= self.db.obtener_proximo_id_cliente()
            self.db.insertar_cliente(id_cliente, nombre, apellido, direccion, telefono, email)
            messagebox.showinfo("Registro Exitoso", f"Cliente {nombre} {apellido} registrado con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")

    
    def registrar_empleado(self, nombre, apellido, cargo, sueldo, ventana):
        if not nombre or not apellido or not cargo or not sueldo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        try:
            id_empleado= self.db.obtener_proximo_id_empleado()
            self.db.insertar_empleado(id_empleado, nombre, apellido, cargo, sueldo)
            messagebox.showinfo("Registro Exitoso", f"Empleado {nombre} {apellido} registrado con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")

    def buscar_habitaciones_disponibles(self, fecha_inicio, fecha_fin):
        return self.db.obtener_habitaciones_disponibles(fecha_inicio, fecha_fin)

    def obtener_clientes(self):
        return self.db.obtener_clientes()

    def abrir_ventana_mostrar_facturas(self):
        facturas = self.db.obtener_facturas_con_detalles()
        self.hotel_app.mostrar_facturas(facturas)
