import tkinter as tk
from tkinter import ttk, messagebox
from Datos.gestor_db import GestorDB
from Entidades.empleado import Empleado


def ventana_registrar_empleado(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Empleado")

    # Campos de entrada
    tk.Label(ventana, text="ID de Empleado:").pack()
    id_empleado_entry = tk.Entry(ventana)
    id_empleado_entry.pack()

    tk.Label(ventana, text=" Nombre :").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tk.Label(ventana, text="Apellido:").pack()
    apellido_entry = tk.Entry(ventana)
    apellido_entry.pack()

    tk.Label(ventana, text="Cargo:").pack()
    cargo_entry = tk.Entry(ventana)
    cargo_entry.pack()

    tk.Label(ventana, text="Sueldo:").pack()
    sueldo_entry = tk.Entry(ventana)
    sueldo_entry.pack()

    # Botón para registrar CLIENTE
    tk.Button(ventana, text="Registrar", command=lambda: registrar_empleado(
        id_empleado_entry.get(), nombre_entry.get(), apellido_entry.get(), cargo_entry.get(), sueldo_entry.get(), ventana, db
    )).pack(pady=10)

def registrar_empleado(id_empleado, nombre, apellido, cargo, sueldo, ventana, db):
    try:
        db.insertar_empleado(id_empleado, nombre, apellido, cargo, sueldo)
        messagebox.showinfo("Registro Exitoso", f"Empleado {nombre} {apellido} registrado con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")

def ventana_ver_empleados(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Lista de Empleados")

    empleados = db.obtener_empleados()
    for empleado in empleados:
        tk.Label(ventana, text=f"ID: {empleado[0]}, Nombre: {empleado[1]}, Apellido: {empleado[2]}, Cargo: {empleado[3]}, Sueldo: {empleado[4]}").pack()

# Asegúrate de cerrar la conexión a la base de datos al finalizar