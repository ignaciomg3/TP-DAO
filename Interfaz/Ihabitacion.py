import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Entidades.habitacion import Habitacion

def ventana_registrar_habitacion(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Habitación")

    # Campos de entrada
    ttk.Label(ventana, text="Número de Habitación:").pack()
    numero_entry = ttk.Entry(ventana)
    numero_entry.pack()

    ttk.Label(ventana, text="Tipo de Habitación:").pack()
    tipo_entry = ttk.Entry(ventana)
    tipo_entry.pack()

    ttk.Label(ventana, text="Estado (disponible/ocupada):").pack()
    estado_entry = ttk.Entry(ventana)
    estado_entry.pack()

    ttk.Label(ventana, text="Precio por Noche:").pack()
    precio_entry = ttk.Entry(ventana)
    precio_entry.pack()

    # Botón para registrar habitación
    ttk.Button(ventana, text="Registrar", command=lambda: registrar_habitacion(
        numero_entry.get(), tipo_entry.get(), estado_entry.get(), precio_entry.get(), ventana, db
    )).pack(pady=10)

def registrar_habitacion(numero, tipo, estado, precio, ventana, db):
    try:
        numero = int(numero)
        precio = float(precio)
        habit = Habitacion(numero, tipo, estado, precio)
        db.insertar_habitacion(habit.numero, habit.tipo, habit.estado, habit.precio_por_noche)
        messagebox.showinfo("Registro Exitoso", f"Habitación {numero} registrada con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")
