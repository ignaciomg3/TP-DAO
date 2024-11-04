import tkinter as tk
from tkinter import ttk
from Datos.gestor_db import GestorDB
from Interfaz.Ihabitacion import *
from Interfaz.Imostrar_habtiaciones import *
#from Iclientes import ventana_ver_habitaciones

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor Hotel")
        self.db = GestorDB()

        # Botones en la ventana principal
        ttk.Button(root, text="Registrar Nueva Habitación", command=self.abrir_ventana_registrar).pack(pady=10)
        ttk.Button(root, text="Ver Habitaciones", command=self.abrir_ventana_ver_habitaciones).pack(pady=10)

    def abrir_ventana_registrar(self):
        ventana_registrar_habitacion(self.root, self.db)

    def abrir_ventana_ver_habitaciones(self):
        ventana_ver_habitaciones(self.root, self.db)
