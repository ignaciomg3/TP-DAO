import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta

def ventana_registrar_reserva(root, gestorI):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Reserva")

    # Estilo de la ventana
    ventana.minsize(400, 400)
    ventana.geometry("400x450")
    ventana.configure(bg="#f0f0f0")  # Fondo suave

    # Crear un marco para agrupar los componentes
    frame = ttk.Frame(ventana, padding=10)
    frame.pack(fill="both", expand=True)

    # Campo para seleccionar fecha de inicio con un calendario
    ttk.Label(frame, text="Fecha de Inicio:", font=("Helvetica", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    fecha_inicio_entry = DateEntry(frame, font=("Helvetica", 10), date_pattern='dd-mm-yyyy', mindate=datetime.now())
    fecha_inicio_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Campo para seleccionar fecha de fin con un calendario
    ttk.Label(frame, text="Fecha de Fin:", font=("Helvetica", 10)).grid(row=0, column=2, padx=5, pady=5, sticky="w")
    fecha_fin_entry = DateEntry(frame, font=("Helvetica", 10), date_pattern='dd-mm-yyyy', mindate=datetime.now() + timedelta(days=1))
    fecha_fin_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    # Botón para buscar habitaciones disponibles
    def buscar_habitaciones():
        fecha_inicio = fecha_inicio_entry.get_date().strftime('%Y-%m-%d')
        fecha_fin = fecha_fin_entry.get_date().strftime('%Y-%m-%d')
        if fecha_fin <= fecha_inicio:
            tk.messagebox.showerror("Error", "La fecha de salida debe ser mayor a la fecha de entrada.")
            return
        global habitaciones_opciones
        habitaciones_opciones = gestorI.buscar_habitaciones_disponibles(fecha_inicio, fecha_fin)
        habitacion_var.set(next(iter(habitaciones_opciones)))  # Establecer opción predeterminada
        habitacion_menu['menu'].delete(0, 'end')
        for habitacion in habitaciones_opciones:
            habitacion_menu['menu'].add_command(label=habitacion, command=tk._setit(habitacion_var, habitacion))

    ttk.Button(frame, text="Buscar Habitaciones Disponibles", command=buscar_habitaciones).grid(row=1, column=0, columnspan=4, pady=10)

    # Campo para seleccionar habitación
    ttk.Label(frame, text="Habitación:", font=("Helvetica", 10)).grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    habitacion_var = tk.StringVar(ventana)
    habitacion_menu = ttk.OptionMenu(frame, habitacion_var, "")
    habitacion_menu.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    # Campo para seleccionar cliente
    ttk.Label(frame, text="Cliente:", font=("Helvetica", 10)).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    cliente_var = tk.StringVar(ventana)
    clientes_opciones = {f"{cliente[1]} {cliente[2]}": cliente[0] for cliente in gestorI.obtener_clientes()}
    cliente_var.set(next(iter(clientes_opciones)))  # Establecer opción predeterminada
    cliente_menu = ttk.OptionMenu(frame, cliente_var, *clientes_opciones.keys())
    cliente_menu.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    # Campo para ingresar la cantidad de personas
    ttk.Label(frame, text="Cantidad de Personas:", font=("Helvetica", 10)).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    cant_personas_entry = ttk.Entry(frame, font=("Helvetica", 10))
    cant_personas_entry.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    def registrar_reserva():
        datos = {
            "id_cliente": clientes_opciones[cliente_var.get()],
            "id_habitacion": habitaciones_opciones[habitacion_var.get()],
            "fecha_inicio": fecha_inicio_entry.get_date().strftime('%Y-%m-%d'),
            "fecha_fin": fecha_fin_entry.get_date().strftime('%Y-%m-%d'),
            "cant_personas": cant_personas_entry.get()
        }
        gestorI.registrar_reserva(datos["id_cliente"], datos["id_habitacion"], datos["fecha_inicio"], datos["fecha_fin"], datos["cant_personas"], ventana)

    # Botón para registrar la reserva
    ttk.Button(
        frame,
        text="Registrar",
        command=registrar_reserva
    ).grid(row=5, column=0, columnspan=4, pady=10)
