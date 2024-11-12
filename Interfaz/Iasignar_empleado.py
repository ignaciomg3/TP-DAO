import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from Entidades.empleado import Empleado

def ventana_asignar_empleado(root, gestor, empleados_limpieza):
    ventana = tk.Toplevel(root)
    ventana.title("Asignar Empleado a Habitación")

    estilo_boton = ttk.Style()
    estilo_boton.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50", foreground="black")
    estilo_boton.map("TButton", background=[("active", "#0b8ad8")], foreground=[("active", "black")])

    tk.Label(ventana, text="Fecha:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)
    fecha_entry = DateEntry(
        ventana, 
        width=12, 
        background='black', 
        foreground='white', 
        borderwidth=2, 
        date_pattern='dd/MM/yyyy',  # Mostrar fecha en formato d/m/y
        showweeknumbers=False,  # Ocultar números de semana
        showothermonthdays=False,  # Ocultar días de otros meses
        selectbackground='blue', 
        selectforeground='white', 
        normalbackground='white', 
        normalforeground='black', 
        disabledbackground='black', 
        disabledforeground='grey', 
        weekendbackground='lightblue', 
        weekendforeground='black', 
        othermonthbackground='lightgrey', 
        othermonthforeground='lightgrey', 
        othermonthwebackground='lightgrey', 
        othermonthweforeground='lightgrey'
    )
    fecha_entry.grid(row=0, column=1, padx=10, pady=10)

    buscar_button = ttk.Button(ventana, text="Buscar Habitaciones", command=lambda: buscar_habitaciones_para_limpieza())
    buscar_button.grid(row=0, column=2, padx=10, pady=10)

    label_habitacion = tk.Label(ventana, text="Habitación:", font=("Helvetica", 12))
    label_habitacion.grid(row=1, column=0, padx=10, pady=10)
    habitaciones_combo = ttk.Combobox(ventana)
    habitaciones_combo.grid(row=1, column=1, padx=10, pady=10)

    label_empleado = tk.Label(ventana, text="Empleado:", font=("Helvetica", 12))
    label_empleado.grid(row=2, column=0, padx=10, pady=10)
    empleados_combo = ttk.Combobox(ventana)
    empleados_combo.grid(row=2, column=1, padx=10, pady=10)
    empleados_combo['values'] = [f"{e.id_empleado} - {e.nombre} {e.apellido}" for e in empleados_limpieza]

    asignar_button = ttk.Button(ventana, text="Asignar Limpieza", command=lambda: asignar_limpieza())
    asignar_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    # Ocultar los elementos hasta que se realice la búsqueda
    label_habitacion.grid_remove()
    habitaciones_combo.grid_remove()
    label_empleado.grid_remove()
    empleados_combo.grid_remove()
    asignar_button.grid_remove()

    def buscar_habitaciones_para_limpieza():
        fecha = fecha_entry.get()
        habitaciones = gestor.buscar_habitaciones_disponibles(fecha, fecha)
        habitaciones_combo['values'] = [f"{h.split('-')[0]} - {h.split('-')[1]}" for h in habitaciones.keys()]

        # Mostrar los elementos después de la búsqueda
        label_habitacion.grid()
        habitaciones_combo.grid()
        label_empleado.grid()
        empleados_combo.grid()
        asignar_button.grid()

    def asignar_limpieza():
        fecha = fecha_entry.get()
        id_habitacion = habitaciones_combo.get().split(" - ")[0]
        id_empleado = empleados_combo.get().split(" - ")[0]
        gestor.registrar_servicio_limpieza(id_empleado, id_habitacion, fecha, ventana)