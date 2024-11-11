import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta

def set_window_icon(window, icon_path='icons/icono.ico'):
    try:
        window.iconbitmap(icon_path)
    except tk.TclError:
        print("No se pudo cargar el icono.")

def ventana_registrar_reserva(root, gestorI):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Reserva")
    set_window_icon(ventana)

    # Estilo de la ventana
    ventana.minsize(400, 400)
    ventana.geometry("500x450")
    ventana.configure(bg="#f0f0f0")  # Fondo suave

    # Crear un marco para agrupar los componentes
    frame = ttk.Frame(ventana, padding=10)
    frame.pack(fill="both", expand=True)

    # Campo para seleccionar fecha de inicio con un calendario
    ttk.Label(frame, text="Fecha de Inicio:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    fecha_inicio_entry = DateEntry(frame, font=("Helvetica", 10), 
                                   date_pattern='dd-mm-yyyy', 
                                   mindate=datetime.now(), 
                                   background='darkblue', 
                                   foreground='white',
                                   showweeknumbers=False, 
                                   borderwidth=2, 
                                   showothermonthdays=False, 
                                   weekendbackground='lightblue')
    fecha_inicio_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Campo para seleccionar fecha de fin con un calendario
    ttk.Label(frame, text="Fecha de Fin:", font=("Helvetica", 10, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky="w")
    fecha_fin_entry = DateEntry(frame, 
                                font=("Helvetica", 10), 
                                date_pattern='dd-mm-yyyy', 
                                mindate=datetime.now() + timedelta(days=1), 
                                background='darkblue', foreground='white', 
                                borderwidth=2, 
                                showothermonthdays=False, 
                                weekendbackground='lightblue')
    fecha_fin_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    # Botón para buscar habitaciones disponibles
    def buscar_habitaciones():
        #Toma los valores de las fechas seleccionadas
        fecha_inicio = fecha_inicio_entry.get_date().strftime('%Y-%m-%d')
        fecha_fin = fecha_fin_entry.get_date().strftime('%Y-%m-%d')
        #Valida que la fecha de salida sea mayor a la fecha de entrada
        if fecha_fin <= fecha_inicio:
            tk.messagebox.showerror("Error", "La fecha de salida debe ser mayor a la fecha de entrada.")
            return
        #Obtiene las habitaciones disponibles en las fechas seleccionadas
        global habitaciones_opciones
        habitaciones_opciones = gestorI.buscar_habitaciones_disponibles(fecha_inicio, fecha_fin)
        habitacion_var.set(next(iter(habitaciones_opciones)))  # Establecer opción predeterminada
        # Muestra los campos ocultos
        habitacion_menu['menu'].delete(0, 'end')
        for habitacion in habitaciones_opciones:
            habitacion_menu['menu'].add_command(label=habitacion, command=tk._setit(habitacion_var, habitacion))
        
        # Mostrar campos ocultos
        habitacion_label.grid()
        habitacion_menu.grid()
        cliente_label.grid()
        cliente_menu.grid()
        cant_personas_label.grid()
        cant_personas_menu.grid()
        registrar_button.grid()

    ttk.Button(frame, text="Buscar Habitaciones Disponibles", command=buscar_habitaciones).grid(row=1, column=0, columnspan=4, pady=10)

    # Campo para seleccionar habitación
    habitacion_label = ttk.Label(frame, text="Habitación:", font=("Helvetica", 10, "bold"))
    habitacion_var = tk.StringVar(ventana)
    habitacion_menu = ttk.OptionMenu(frame, habitacion_var, "")
    habitacion_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    habitacion_menu.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
    habitacion_label.grid_remove()
    habitacion_menu.grid_remove()

    # Campo para seleccionar cliente
    cliente_label = ttk.Label(frame, text="Cliente:", font=("Helvetica", 10, "bold"))
    cliente_var = tk.StringVar(ventana)
    clientes_opciones = {f"{cliente[1]} {cliente[2]}": cliente[0] for cliente in gestorI.obtener_clientes()}
    cliente_var.set(next(iter(clientes_opciones)))  # Establecer opción predeterminada
    cliente_menu = ttk.OptionMenu(frame, cliente_var, *clientes_opciones.keys())
    cliente_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    cliente_menu.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
    cliente_label.grid_remove()
    cliente_menu.grid_remove()

    # Campo para ingresar la cantidad de personas
    # Campo para seleccionar la cantidad de personas
    cant_personas_label = ttk.Label(frame, text="Cantidad de Personas:", font=("Helvetica", 10, "bold"))
    cant_personas_var = tk.StringVar(ventana)
    cant_personas_menu = ttk.OptionMenu(frame, cant_personas_var, "1", "1", "2", "3", "4", "5")
    
    # Posicionar el label y el combo box en la grilla
    cant_personas_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    cant_personas_menu.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
    
    # Ocultar los campos inicialmente
    cant_personas_label.grid_remove()
    cant_personas_menu.grid_remove()



    def registrar_reserva():
        datos = {
            "id_cliente": clientes_opciones[cliente_var.get()],
            "id_habitacion": habitaciones_opciones[habitacion_var.get()],
            "fecha_inicio": fecha_inicio_entry.get_date().strftime('%Y-%m-%d'),
            "fecha_fin": fecha_fin_entry.get_date().strftime('%Y-%m-%d'),
            "cant_personas": cant_personas_var.get()
        }
        print("Datos de la reserva:")
        print(f"ID Cliente: {datos['id_cliente']}")
        print(f"ID Habitación: {datos['id_habitacion']}")
        print(f"Fecha de Inicio: {datos['fecha_inicio']}")
        print(f"Fecha de Fin:       {datos['fecha_fin']}")
        print(f"Cantidad de Personas: {datos['cant_personas']}")
        gestorI.registrar_reserva(datos["id_cliente"],
                                   datos["id_habitacion"],
                                     datos["fecha_inicio"],
                                       datos["fecha_fin"],
                                         datos["cant_personas"], ventana)

    # Botón para registrar la reserva
    registrar_button = ttk.Button(
        frame,
        text="Registrar",
        command=registrar_reserva
    )
    registrar_button.grid(row=5, column=0, columnspan=4, pady=10)
    registrar_button.grid_remove()
