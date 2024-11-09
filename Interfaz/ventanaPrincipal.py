import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from Datos.gestor_db import GestorDB
from Interfaz.Ihabitacion import *
from Interfaz.Imostrar_habitaciones import *
from Interfaz.Iclientes import *
from Interfaz.Ireserva import *
from Interfaz.Iempleados import *
from Interfaz.Ireserva import *
from Interfaz.Ireportes import *

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor Hotel")
        self.root.geometry("1280x720")
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

        # Crear fuente de íconos
        icon_font = Font(family="Google Icons", size=16)

        # Diccionario de íconos
        self.iconos = {
            "habitacion": "\ue88a",  # Icono de habitación
            "ver_habitaciones": "\ue8b6",  # Icono de ver habitaciones
            "cliente": "\ue7fd",  # Icono de cliente
            "ver_clientes": "\ue8a1",  # Icono de ver clientes
            "reserva": "\ue8b0",  # Icono de reserva
            "empleado": "\ue7fb",  # Icono de empleado
            "ver_empleados": "\ue8a3",  # Icono de ver empleados
            "reportes": "\ue85c"  # Icono de reportes
        }

        # Botones en la ventana principal
        botones = [
            ("Registrar Nueva Habitación", self.abrir_ventana_registrar, self.iconos["habitacion"]),
            ("Ver Habitaciones", self.abrir_ventana_ver_habitaciones, self.iconos["ver_habitaciones"]),
            ("Registrar Nuevo Cliente", self.abrir_ventana_registrar_cliente, self.iconos["cliente"]),
            ("Ver Clientes", self.abrir_ventana_ver_clientes, self.iconos["ver_clientes"]),
            ("Registrar Reservas", self.abrir_ventana_registrar_reserva, self.iconos["reserva"]),
            ("Registrar Empleado", self.abrir_ventana_registrar_empleado, self.iconos["empleado"]),
            ("Ver Empleados", self.abrir_ventana_ver_empleados, self.iconos["ver_empleados"]),
            ("Reportes", self.abrir_ventana_reportes, self.iconos["reportes"])
        ]

        # Crear un frame para los botones
        frame_botones = ttk.Frame(root, style="Card.TFrame")
        frame_botones.pack(fill="both", expand=True, padx=20, pady=20)

        # Configurar el grid para que sea responsive
        columnas = 3
        for i in range(columnas):
            frame_botones.columnconfigure(i, weight=1)
        for i in range((len(botones) + columnas - 1) // columnas):
            frame_botones.rowconfigure(i, weight=1)

        # Distribuir los botones en una cuadrícula
        for i, (texto, comando, icono) in enumerate(botones):
            fila = i // columnas
            columna = i % columnas
            self.crear_tarjeta(frame_botones, texto, comando, icono, icon_font, fila, columna)

    def crear_tarjeta(self, parent, texto, comando, icono, icon_font, fila, columna):
        frame = ttk.Frame(parent, style="Card.TFrame", padding=(10, 10))
        frame.grid(row=fila, column=columna, padx=20, pady=20, sticky="nsew")

        label_icono = ttk.Label(frame, text=icono, font=icon_font, style="Card.TLabel")
        label_icono.pack(side="left", padx=(0, 10))

        boton = ttk.Button(frame, text=texto, command=comando, style="Card.TButton")
        boton.pack(side="left", fill="x", expand=True)

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

    def abrir_ventana_reportes(self):
        ventana_reportes(self.root, self.db)
