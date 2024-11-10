import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Entidades.habitacion import Habitacion

def ventana_registrar_habitacion(gestor, root):
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

    # Función para registrar la habitación
    def confirmar_registro():
        numero = numero_entry.get()
        tipo = tipo_entry.get()
        estado = estado_entry.get()
        precio = precio_entry.get()

        habitacion = registrar_habitacion(numero, tipo, estado, precio)

        if habitacion:  # Solo proceder si se creó el objeto exitosamente
            try:
                # Usamos el gestor para registrar la habitación
                gestor.registrar_habitacion(habitacion.numero, habitacion.tipo, habitacion.estado, habitacion.precio_por_noche, ventana)
            except AttributeError:
                messagebox.showerror("Error", "El método registrar_habitacion no está definido en GestorInterfaces.")

    ttk.Button(ventana, text="Registrar", command=confirmar_registro).pack(pady=10)

def registrar_habitacion(numero, tipo, estado, precio):
    # Verificar si algún campo está vacío
    if not all([numero, tipo, estado, precio]):
        messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos antes de registrar.")
        return None
    
    # Validación del número de habitación
    try:
        numero = int(numero)
        if not (1 <= numero <= 100):
            messagebox.showerror("Error", "Ingrese un número de habitación válido (1-100).")
            return None
    except ValueError:
        messagebox.showerror("Error", "El número de habitación debe ser un número entero.")
        return None

    # Validación del precio
    try:
        precio = float(precio)
        if precio <= 0:
            messagebox.showerror("Error", "El precio debe ser un número positivo.")
            return None
    except ValueError:
        messagebox.showerror("Error", "El precio debe ser un número válido.")
        return None

    # Crear el objeto Habitacion solo si todas las validaciones son exitosas
    habit = Habitacion(numero, tipo, estado, precio)
    
    return habit
