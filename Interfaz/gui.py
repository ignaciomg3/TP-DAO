import tkinter as tk
from tkinter import ttk
from Datos.gestor_db import GestorDB
from Interfaz.Ihabitacion import *
from Interfaz.Imostrar_habtiaciones import *
from Interfaz.Iclientes import *
from Interfaz.Ireserva import *
from Interfaz.Iempleados import *

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor Hotel")
        self.db = GestorDB()
        self.db.borrar_base_de_datos()
        self.db.crear_tablas()    


        # Botones en la ventana principal
        ttk.Button(root, text="Registrar Nueva Habitación", command=self.abrir_ventana_registrar).pack(pady=10)
        ttk.Button(root, text="Ver Habitaciones", command=self.abrir_ventana_ver_habitaciones).pack(pady=10)
        ttk.Button(root, text="Registrar Nuevo Cliente", command=self.abrir_ventana_registrar_cliente).pack(pady=10)
        ttk.Button(root, text="Ver Clientes", command=self.abrir_ventana_ver_clientes).pack(pady=10)
        ttk.Button(root, text="Registrar Reservas", command=self.abrir_ventana_registrar_reserva).pack(pady=10)
        ttk.Button(root, text="Ver Empleados", command=self.abrir_ventana_ver_empleados).pack(pady=10)
        ttk.Button(root, text="Registrar Empleado", command=self.abrir_ventana_registrar_empleado).pack(pady=10)
        #ttk.Button(root, text="Ver Reservas", command=self.abrir_ventana_ver_reservas).pack(pady=10)

    def abrir_ventana_registrar(self):
        ventana_registrar_habitacion(self.root, self.db)

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
    #def abrir_ventana_ver_reservas(self):
    #    ventana_ver_reservas(self.root, self.db)