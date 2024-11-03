import tkinter as tk
from tkinter import ttk, messagebox
from Datos.gestor_db import GestorDB
from Entidades.habitacion import Habitacion

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor Hotel")
        self.db = GestorDB()

        # Botones en la ventana principal
        ttk.Button(root, text="Registrar Nueva Habitación", command=self.ventana_registrar_habitacion).pack(pady=10)
        ttk.Button(root, text="Ver Habitaciones", command=self.ventana_ver_habitaciones).pack(pady=10)

    def ventana_registrar_habitacion(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Habitación")

        # Campos de entrada
        tk.Label(ventana, text="Número de Habitación:").pack()
        numero_entry = tk.Entry(ventana)
        numero_entry.pack()

        tk.Label(ventana, text="Tipo de Habitación:").pack()
        tipo_entry = tk.Entry(ventana)
        tipo_entry.pack()

        tk.Label(ventana, text="Estado (disponible/ocupada):").pack()
        estado_entry = tk.Entry(ventana)
        estado_entry.pack()

        tk.Label(ventana, text="Precio por Noche:").pack()
        precio_entry = tk.Entry(ventana)
        precio_entry.pack()

        # Botón para registrar habitación
        tk.Button(ventana, text="Registrar", command=lambda: self.registrar_habitacion(
            numero_entry.get(), tipo_entry.get(), estado_entry.get(), precio_entry.get(), ventana
        )).pack(pady=10)

    def registrar_habitacion(self, numero, tipo, estado, precio, ventana):
        try:
            numero = int(numero)
            precio = float(precio)
            tipo = int(tipo)
            estado = int(estado)
            habit = Habitacion(numero, tipo, estado, precio)
            self.db.insertar_habitacion(habit)
            messagebox.showinfo("Registro Exitoso", f"Habitación {numero} registrada con éxito.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese datos válidos.")

    def ventana_ver_habitaciones(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Lista de Habitaciones")

        habitaciones = self.db.obtener_habitaciones()
        for habitacion in habitaciones:
            tk.Label(ventana, text=f"Nro: {habitacion[0]}, Tipo: {habitacion[1]}, Estado: {habitacion[2]}, Precio: {habitacion[3]}").pack()

# Asegúrate de cerrar la conexión a la base de datos al finalizar
