import tkinter as tk
from tkinter import messagebox
from Entidades.reserva import Reserva

def ventana_registrar_reserva(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Reserva")

    # Obtener habitaciones y clientes desde la base de datos
    habitaciones = db.obtener_habitaciones_para_reserva()
    clientes = db.obtener_clientes()

    # Transformar los datos para mostrar texto y almacenar el ID correspondiente
    habitaciones_opciones = {f"{habitacion[0]}-{habitacion[1]}": habitacion[0] for habitacion in habitaciones}  # Ejemplo: "102-simple": 102
    clientes_opciones = {f"{cliente[1]} {cliente[2]}": cliente[0] for cliente in clientes}  # Ejemplo: "Juan Perez": 1

    # Campo para seleccionar habitación
    tk.Label(ventana, text="Habitación:").pack()
    habitacion_var = tk.StringVar(ventana)
    habitacion_var.set(next(iter(habitaciones_opciones)))  # Establecer opción predeterminada
    habitacion_menu = tk.OptionMenu(ventana, habitacion_var, *habitaciones_opciones.keys())
    habitacion_menu.pack()

    # Campo para seleccionar cliente
    tk.Label(ventana, text="Cliente:").pack()
    cliente_var = tk.StringVar(ventana)
    cliente_var.set(next(iter(clientes_opciones)))  # Establecer opción predeterminada
    cliente_menu = tk.OptionMenu(ventana, cliente_var, *clientes_opciones.keys())
    cliente_menu.pack()

    # Campos de entrada para las fechas y la cantidad de personas
    tk.Label(ventana, text="Fecha de Inicio (YYYY-MM-DD):").pack()
    fecha_inicio_entry = tk.Entry(ventana)
    fecha_inicio_entry.pack()

    tk.Label(ventana, text="Fecha de Fin (YYYY-MM-DD):").pack()
    fecha_fin_entry = tk.Entry(ventana)
    fecha_fin_entry.pack()

    tk.Label(ventana, text="Cantidad de Personas:").pack()
    cant_personas_entry = tk.Entry(ventana)
    cant_personas_entry.pack()

    # Botón para registrar la reserva
    tk.Button(
        ventana,
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
        # Guardar en la base de datos
        db.insertar_reserva(1,id_cliente, id_habitacion, fecha_inicio, fecha_fin, cant_personas)
        consulta = "UPDATE habitaciones SET estado = 'ocupado' WHERE numero = ?"
        parametros = (id_habitacion, )
        db.ejecutar_consulta(consulta, parametros)
        messagebox.showinfo("Registro Exitoso", "Reserva registrada con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar la reserva: {e}")
