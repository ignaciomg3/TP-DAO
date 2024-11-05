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
        self.root.geometry("400x500")
        self.root.config(bg="#2b3e50")  # Fondo azul oscuro

        self.db = GestorDB()
        self.db.borrar_base_de_datos()
        self.db.crear_tablas()

        # Título principal
        ttk.Label(root, text="Gestión del Hotel", font=("Helvetica", 18, "bold"), foreground="white", background="#2b3e50").pack(pady=(20, 20))

        # Estilo de botones
        estilo_boton = ttk.Style()
        estilo_boton.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50", foreground="black")
        estilo_boton.map("TButton", background=[("active", "#0b8ad8")], foreground=[("active", "black")])

        # Botones en la ventana principal
        botones = [
            ("Registrar Nueva Habitación", self.abrir_ventana_registrar),
            ("Ver Habitaciones", self.abrir_ventana_ver_habitaciones),
            ("Registrar Nuevo Cliente", self.abrir_ventana_registrar_cliente),
            ("Ver Clientes", self.abrir_ventana_ver_clientes),
            ("Registrar Reservas", self.abrir_ventana_registrar_reserva),
            ("Ver Empleados", self.abrir_ventana_ver_empleados),
            ("Registrar Empleado", self.abrir_ventana_registrar_empleado)
        ]

        for texto, comando in botones:
            ttk.Button(root, text=texto, command=comando, style="TButton").pack(fill="x", padx=40, pady=5)

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
