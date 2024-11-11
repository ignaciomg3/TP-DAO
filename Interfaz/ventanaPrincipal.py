import tkinter as tk
from tkinter import ttk
from Datos.gestor_db import GestorDB
#from Interfaz.gestorInterfaces import *

class HotelApp:
    def __init__(self, root, gestorI):
        self.root = root
        self.root.title("Gestor Hotel")
        self.root.geometry("1280x720")
        self.root.config(bg="#2b3e50")  # Fondo azul oscuro
        self.root.iconbitmap('icons/icono.ico')

        # Center the window on the screen
        self.center_window(1280, 720)

        self.gestorI = gestorI

        # Título principal
        ttk.Label(root, text="Gestión del Hotel", font=("Helvetica", 18, "bold"), foreground="white", background="#2b3e50").pack(pady=(20, 20))

        # Estilo de botones
        estilo_boton = ttk.Style()
        estilo_boton.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50", foreground="black")
        estilo_boton.map("TButton", background=[("active", "#0b8ad8")], foreground=[("active", "black")])

        # Cargar iconos
        self.iconos = {
            "habitacion": tk.PhotoImage(file="icons/habitacion.png"),
            "ver_habitaciones": tk.PhotoImage(file="icons/ver_habitacion.png"),
            "cliente": tk.PhotoImage(file="icons/cliente.png"),
            "ver_clientes": tk.PhotoImage(file="icons/ver_clientes.png"),
            "reserva": tk.PhotoImage(file="icons/reserva.png"),
            "empleado": tk.PhotoImage(file="icons/empleado.png"),
            "ver_empleados": tk.PhotoImage(file="icons/ver_empleados.png"),
            "reportes": tk.PhotoImage(file="icons/reportes.png")
        }

        # Guardar referencias a las imágenes para evitar que sean recolectadas por el recolector de basura
        self.icon_refs = list(self.iconos.values())

        # Botones en la ventana principal
        botones = [
            ("Registrar Nueva Habitación", lambda: gestorI.abrir_ventana_registrar_habitacion(), self.iconos["habitacion"]),
            ("Ver Habitaciones", lambda: gestorI.abrir_ventana_ver_habitaciones(), self.iconos["ver_habitaciones"]),
            ("Registrar Nuevo Cliente", lambda: gestorI.abrir_ventana_registrar_cliente(), self.iconos["cliente"]),
            ("Ver Clientes", lambda: gestorI.abrir_ventana_ver_clientes(), self.iconos["ver_clientes"]),
            ("Registrar Reservas", lambda: gestorI.abrir_ventana_registrar_reserva(), self.iconos["reserva"]),
            ("Registrar Empleado", lambda: gestorI.abrir_ventana_registrar_empleado(), self.iconos["empleado"]),
            ("Ver Empleados", lambda: gestorI.abrir_ventana_ver_empleados(), self.iconos["ver_empleados"]),
            ("Reportes", lambda: gestorI.abrir_ventana_reportes(), self.iconos["reportes"])
        ]

        # Crear un frame para los botones
        frame_botones = ttk.Frame(root, style="Card.TFrame")
        frame_botones.pack(fill="both", expand=True, padx=20, pady=20)
        frame_botones.configure(style="Card.TFrame")  # Aplicar estilo

        # Configurar el estilo para el fondo
        estilo_frame = ttk.Style()
        estilo_frame.configure("Card.TFrame", background="#97C4B8")

        # Configurar el grid para que sea responsive
        columnas = 3
        for i in range(columnas):
            frame_botones.columnconfigure(i, weight=1)
        for i in range((len(botones) + columnas - 1) // columnas):
            frame_botones.rowconfigure(i, weight=1)

        # Distribuir los botones en una cuadrícula
        for i, (texto, comando, icono) in enumerate(botones):
            fila = i // columnas
            columna = i % columnas
            self.crear_tarjeta(frame_botones, texto, comando, icono, fila, columna)

    def crear_tarjeta(self, parent, texto, comando, icono, fila, columna):
        frame = ttk.Frame(parent, style="Card.TFrame", padding=(10, 10))
        frame.grid(row=fila, column=columna, padx=20, pady=20, sticky="nsew")
        frame.configure(style="Card.TFrame")  # Aplicar estilo

        label_icono = ttk.Label(frame, image=icono, style="Card.TLabel")
        label_icono.pack(side="top", pady=(0, 10))

        boton = ttk.Button(frame, text=texto, command=comando, style="Card.TButton")
        boton.pack(side="top", fill="x", expand=True)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def mostrarPantalla(self):
        self.root.mainloop()