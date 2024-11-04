import tkinter as tk

def ventana_ver_habitaciones(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Lista de Habitaciones")

    habitaciones = db.obtener_habitaciones()
    for habitacion in habitaciones:
        tk.Label(ventana, text=f"Nro: {habitacion[0]}, Tipo: {habitacion[1]}, Estado: {habitacion[2]}, Precio: {habitacion[3]}").pack()
