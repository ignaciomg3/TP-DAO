import tkinter as tk
from tkinter import ttk, messagebox
from Datos.gestor_db import GestorDB
from Entidades.cliente import Cliente


def ventana_registrar_cliente(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Cliente")

    # Campos de entrada
    tk.Label(ventana, text="ID de Cliente:").pack()
    id_cliente_entry = tk.Entry(ventana)
    id_cliente_entry.pack()

    tk.Label(ventana, text=" Nombre :").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tk.Label(ventana, text="Apellido:").pack()
    apellido_entry = tk.Entry(ventana)
    apellido_entry.pack()

    tk.Label(ventana, text="Dirección:").pack()
    direccion_entry = tk.Entry(ventana)
    direccion_entry.pack()

    tk.Label(ventana, text="Telefono:").pack()
    telefono_entry = tk.Entry(ventana)
    telefono_entry.pack()

    tk.Label(ventana, text="Email:").pack()
    email_entry = tk.Entry(ventana)
    email_entry.pack()

    # Botón para registrar CLIENTE
    tk.Button(ventana, text="Registrar", command=lambda: registrar_cliente(
        id_cliente_entry.get(), nombre_entry.get(), apellido_entry.get(), direccion_entry.get(), telefono_entry.get(), email_entry.get(), ventana, db
    )).pack(pady=10)

def registrar_cliente(id_cliente, nombre, apellido, direccion, telefono, email, ventana, db):
    try:
        db.insertar_cliente(id_cliente, nombre, apellido, direccion, telefono, email)
        messagebox.showinfo("Registro Exitoso", f"Cliente {nombre} {apellido} registrado con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")

def ventana_ver_clientes(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Lista de Clientes")

    clientes = db.obtener_clientes()
    for cliente in clientes:
        tk.Label(ventana, text=f"ID: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Direccion: {cliente[3]}, Telefono: {cliente[4]}, Email: {cliente[5]}").pack()

# Asegúrate de cerrar la conexión a la base de datos al finalizar