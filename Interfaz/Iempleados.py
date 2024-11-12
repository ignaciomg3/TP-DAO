import tkinter as tk
from tkinter import ttk, messagebox
from Interfaz.gestorInterfaces import GestorInterfaces


def ventana_registrar_empleado(root, db, gestor_interfaces):
    ventana = tk.Toplevel(root)
    ventana.minsize(400, 400)
    ventana.geometry("400x400")
    ventana.configure(bg="#f0f0f0")

    # Estilo de etiquetas y entradas
    label_style = {"font": ("Helvetica", 12), "bg": "#f0f0f0"}
    entry_style = {"font": ("Helvetica", 12), "bg": "#ffffff", "bd": 2, "relief": "groove"}

    # Campos de entrada
    tk.Label(ventana, text="ID de Empleado:", **label_style).pack(pady=(10, 5))
    id_empleado_entry = tk.Entry(ventana, **entry_style)
    id_empleado_entry.pack(pady=(0, 10))

    tk.Label(ventana, text="Nombre:", **label_style).pack(pady=(10, 5))
    nombre_entry = tk.Entry(ventana, **entry_style)
    nombre_entry.pack(pady=(0, 10))

    tk.Label(ventana, text="Apellido:", **label_style).pack(pady=(10, 5))
    apellido_entry = tk.Entry(ventana, **entry_style)
    apellido_entry.pack(pady=(0, 10))

    # tk.Label(ventana, text="Cargo:", **label_style).pack(pady=(10, 5))
    # cargo_entry = tk.Entry(ventana, **entry_style)
    # cargo_entry.pack(pady=(0, 10))

    tk.Label(ventana, text="Cargo:", **label_style).pack(pady=(10, 5))
    cargo_combobox = ttk.Combobox(ventana, values=["gerente", "cocinero", "Encargado de Limpieza", "Encargado de Sábanas"], font=("Helvetica", 12))
    cargo_combobox.pack(pady=(0, 10))

    tk.Label(ventana, text="Sueldo:", **label_style).pack(pady=(10, 5))
    sueldo_entry = tk.Entry(ventana, **entry_style)
    sueldo_entry.pack(pady=(0, 10))

    def registrar_empleado():
        datos = {
            "id_empleado": id_empleado_entry.get(),
            "nombre": nombre_entry.get(),
            "apellido": apellido_entry.get(),
            "cargo": cargo_combobox.get(),
            "sueldo": sueldo_entry.get()
        }
        gestor_interfaces.registrar_empleado(datos["id_empleado"], datos["nombre"], datos["apellido"], datos["cargo"], datos["sueldo"], ventana)

    tk.Button(
        ventana, text="Registrar", command=registrar_empleado, font=("Helvetica", 12), bg="#0b8ad8", fg="white", bd=0, relief="flat", padx=10, pady=5
    ).pack(pady=20)

def registrar_empleado(id_empleado, nombre, apellido, cargo, sueldo, ventana, db):
    if not id_empleado or not nombre or not apellido or not cargo or not sueldo:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    try:
        db.insertar_empleado(id_empleado, nombre, apellido, cargo, sueldo)
        messagebox.showinfo("Registro Exitoso", f"Empleado {nombre} {apellido} registrado con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")
        messagebox.showinfo("Registro Exitoso", f"Empleado {nombre} {apellido} registrado con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")

def ventana_ver_empleados(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Lista de Empleados")
    ventana.geometry("900x600+0+0")

    # Título estilizado
    titulo = ttk.Label(ventana, text="Listado de Empleados", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=(10, 5))

    # Crear un marco para la tabla con borde y padding
    frame = ttk.Frame(ventana, padding=10, relief="solid", borderwidth=1)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Estilos para Treeview
    estilo = ttk.Style()
    estilo.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    estilo.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#0b8ad8", foreground="black")
    estilo.map("Treeview", background=[("selected", "#0b8ad8")])

    # Crear el widget Treeview
    columnas = ("id", "nombre", "apellido", "cargo", "sueldo")
    tree = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
    tree.pack(fill="both", expand=True)

    # Definir encabezados de columna
    tree.heading("id", text="ID")
    tree.heading("nombre", text="Nombre")
    tree.heading("apellido", text="Apellido")
    tree.heading("cargo", text="Cargo")
    tree.heading("sueldo", text="Sueldo")

    # Ajustar el ancho de las columnas
    tree.column("id", width=50, anchor="center")
    tree.column("nombre", width=150, anchor="center")
    tree.column("apellido", width=150, anchor="center")
    tree.column("cargo", width=150, anchor="center")
    tree.column("sueldo", width=100, anchor="center")

    # Alternar el color de fondo de las filas
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar datos a la tabla
    empleados = db.obtener_empleados()
    for i, empleado in enumerate(empleados):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=empleado, tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal (opcional, si es necesario)
    h_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=h_scrollbar.set)
    h_scrollbar.pack(side="bottom", fill="x")

# Ejemplo de cómo llamar a la función
# ventana_ver_empleados(root, db)

# Asegúrate de cerrar la conexión a la base de datos al finalizar