#************************ IMPORTS ************************

from Datos.gestor_db import GestorDB

#Importar las clases de las INTERFACES

from Interfaz.Iclientes import *
from Interfaz.Iempleados import *
from Interfaz.Ihabitacion import *
from Interfaz.Ireserva import *
from Interfaz.Ireportes import *
from Interfaz.ventanaPrincipal import *
from Interfaz.Imostrar_habitaciones import *

#Importar clase de ENTIDADES
from Entidades.habitacion import *
from Entidades.cliente import *
from Entidades.empleado import *
from Entidades.reserva import *
from Entidades.factura import *

#Importar librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

import matplotlib.pyplot as plt
from datetime import datetime
from time import sleep


#Clase GestorInterfaces
# def usar_IHabitaciones():
#     habitaciones = HotelApp()
#     habitaciones.listar_habitaciones()
#     #crear gestroBD
     
    
class GestorInterfaces:
    def __init__(self, root, db_parametro):
        self.root = root
        self.db = db_parametro
        self.db.borrar_base_de_datos()
        self.db.crear_tablas()
        

    def abrir_Ventana_Principal(self):
        print("Abriendo ventana principal por gestorInterfaces")
        #1) Crear la ventana principal
        self.root = HotelApp(self.root, self)
        #2) Mostrar la ventana
        self.root.mostrarPantalla()

    def abrir_ventana_registrar_habitacion(self):
         
        #2) habitacion = ventana_registrar_habitacion(self.root, self.db)
        print("Abriendo ventana registrar habitacion")
        habit = ventana_registrar_habitacion(self, self.root)
        #3) Validar algunas cosas (no se me ocurre nada )
        #4) GestorBD.registrar_habitacion(habitacion)
        self.db.insertar_habitacion(habit.numero, habit.tipo, habit.estado, habit.precio)

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