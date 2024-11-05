import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Entidades.reserva import Reserva
from tkcalendar import DateEntry

def ventana_registrar_reserva(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Reserva")

    # Estilo de la ventana
    ventana.minsize(400, 400)
    ventana.geometry("400x450")
    ventana.configure(bg="#f0f0f0")  # Fondo suave

    # Crear un marco para agrupar los componentes
    frame = ttk.Frame(ventana, padding=10)
    frame.pack(fill="both", expand=True)

    # Obtener habitaciones y clientes desde la base de datos
    habitaciones = db.obtener_habitaciones_para_reserva()
    clientes = db.obtener_clientes()

    # Transformar los datos para mostrar texto y almacenar el ID correspondiente
    habitaciones_opciones = {f"{habitacion[0]}-{habitacion[1]}": habitacion[0] for habitacion in habitaciones}  # Ejemplo: "102-simple": 102
    clientes_opciones = {f"{cliente[1]} {cliente[2]}": cliente[0] for cliente in clientes}  # Ejemplo: "Juan Perez": 1

    # Campo para seleccionar habitación
    ttk.Label(frame, text="Habitación:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    habitacion_var = tk.StringVar(ventana)
    habitacion_var.set(next(iter(habitaciones_opciones)))  # Establecer opción predeterminada
    habitacion_menu = ttk.OptionMenu(frame, habitacion_var, *habitaciones_opciones.keys())
    habitacion_menu.pack(fill="x", pady=5)

    # Campo para seleccionar cliente
    ttk.Label(frame, text="Cliente:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    cliente_var = tk.StringVar(ventana)
    cliente_var.set(next(iter(clientes_opciones)))  # Establecer opción predeterminada
    cliente_menu = ttk.OptionMenu(frame, cliente_var, *clientes_opciones.keys())
    cliente_menu.pack(fill="x", pady=5)

    

    # Campo para seleccionar fecha de inicio con un calendario
    ttk.Label(frame, text="Fecha de Inicio:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    fecha_inicio_entry = DateEntry(frame, font=("Helvetica", 10), date_pattern='yyyy-mm-dd')
    fecha_inicio_entry.pack(fill="x", pady=5)       

    # Campo para seleccionar fecha de fin DATEPICKE
    ttk.Label(frame, text="Fecha de Fin:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    fecha_fin_entry = DateEntry(frame, font=("Helvetica", 10), date_pattern='yyyy-mm-dd')
    fecha_fin_entry.pack(fill="x", pady=5)

    

    ttk.Label(frame, text="Cantidad de Personas:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    cant_personas_entry = ttk.Entry(frame, font=("Helvetica", 10))
    cant_personas_entry.pack(fill="x", pady=5)

    # Botón para registrar la reserva
    ttk.Button(
        frame,
        text="Registrar",
        command=lambda: registrar_reserva(
            clientes_opciones[cliente_var.get()],
            habitaciones_opciones[habitacion_var.get()],
            fecha_inicio_entry.get(),
            fecha_fin_entry.get(),
            cant_personas_entry.get(),
            ventana,
            db
        )
    ).pack(pady=10)


def registrar_reserva(id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas, ventana, db):
    try:
        # Validar que ninguno de los parámetros sea nulo
        if not all([id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas]):
            raise ValueError("Todos los campos son obligatorios.")

        # Guardar en la base de datos
        db.insertar_reserva(1, id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas)
        consulta = "UPDATE habitaciones SET estado = 'ocupado' WHERE numero = ?"
        parametros = (id_habitacion, )
        db.ejecutar_consulta(consulta, parametros)
        messagebox.showinfo("Registro Exitoso", "Reserva registrada con éxito.")
        ventana.destroy()
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar la reserva: {e}")
