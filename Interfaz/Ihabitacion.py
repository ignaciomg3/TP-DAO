import tkinter as tk
from tkinter import ttk
# from Interfaz.gestorInterfaces import GestorInterfaces

def ventana_registrar_habitacion(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Habitación")
    ventana.geometry("700x600")
    ventana.configure(bg="#e6f3f5")

    frame = ttk.Frame(ventana, padding=15)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Título estilizado
    ttk.Label(frame, text="Registrar Habitación", font=("Helvetica", 14, "bold")).pack(pady=(0, 10))

    # Campos de entrada estilizados
    ttk.Label(frame, text="Número de Habitación:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    numero_entry = ttk.Entry(frame, font=("Helvetica", 10))
    numero_entry.pack(fill="x", pady=5)

    # Combobox para tipo de habitación
    ttk.Label(frame, text="Tipo de Habitación:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    tipo_entry = ttk.Combobox(frame, font=("Helvetica", 10), 
                              values=["simple", "doble", "suite"],
                            state="readonly")
    tipo_entry.current(0)  # Seleccionar "simple" como valor predeterminado
    tipo_entry.pack(fill="x", pady=5)

    # Campo de estado
    ttk.Label(frame, text="Estado (disponible/ocupada):", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    estado_entry = ttk.Combobox(frame, font=("Helvetica", 10), 
                                values=["disponible", "ocupada"],
                                state="readonly")
    estado_entry.current(0)  # Seleccionar "disponible" como valor predeterminado
    estado_entry.pack(fill="x", pady=5)

    # Campo de precio
    ttk.Label(frame, text="Precio por Noche:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    precio_entry = ttk.Entry(frame, font=("Helvetica", 10))
    precio_entry.pack(fill="x", pady=5)

    def registrar_habitacion():
        datos = {
            "numero": numero_entry.get(),
            "tipo": tipo_entry.get(),
            "estado": estado_entry.get(),
            "precio": precio_entry.get()
        }
        GestorInterfaces().registrar_habitacion(datos["numero"], datos["tipo"], datos["estado"], datos["precio"], ventana)

    ttk.Button(ventana, text="Registrar", command=registrar_habitacion).pack(pady=10)
