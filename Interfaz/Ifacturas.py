import tkinter as tk
from tkinter import ttk
from datetime import datetime

def ventana_mostrar_facturas(root, facturas):
    ventana_facturas = tk.Toplevel(root)
    ventana_facturas.title("Facturas Generadas")
    ventana_facturas.geometry("1200x400")

    columnas = ("nro_reserva", "nombre", "apellido", "numero_habitacion", "fecha_emision", "total")
    tabla = ttk.Treeview(ventana_facturas, columns=columnas, show="headings")
    tabla.heading("nro_reserva", text="Nro Reserva")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("apellido", text="Apellido")
    tabla.heading("numero_habitacion", text="Nro Habitación")
    tabla.heading("fecha_emision", text="Fecha Emisión")
    tabla.heading("total", text="Total")

    for col in columnas:
        tabla.column(col, anchor="center")  # Centrar los datos

    for factura in facturas:
        # Convertir la fecha a formato d-m-y
        fecha_emision = datetime.strptime(factura[4], "%Y-%m-%d").date().strftime("%d-%m-%Y")
        tabla.insert("", "end", values=(factura[0], factura[1], factura[2], factura[3], fecha_emision, factura[5]))

    tabla.pack(fill="both", expand=True)