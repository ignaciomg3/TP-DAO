import tkinter as tk
from tkinter import ttk, messagebox
from Interfaz.gestorInterfaces import *
from Entidades.cliente import Cliente


def ventana_registrar_cliente(root, db, gestor_interfaces):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Cliente")
    ventana.geometry("400x650")
    ventana.configure(bg="#e6f3f5")
    ventana.transient(root)  # Mantener la ventana siempre adelante
    ventana.grab_set()  # Bloquear la interacción con otras ventanas hasta que esta se cierre

    # Crear un marco con padding y estilo
    frame = ttk.Frame(ventana, padding=15)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Título estilizado
    ttk.Label(frame, text="Registrar Cliente", font=("Helvetica", 14, "bold")).pack(pady=(0, 10))

    # ID de Cliente
    #ttk.Label(frame, text="ID de Cliente:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    #id_cliente_entry = ttk.Entry(frame, font=("Helvetica", 10))
    #id_cliente_entry.pack(fill="x", pady=5)

    # Nombre
    ttk.Label(frame, text="Nombre:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    nombre_entry = ttk.Entry(frame, font=("Helvetica", 10))
    nombre_entry.pack(fill="x", pady=5)

    # Apellido
    ttk.Label(frame, text="Apellido:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    apellido_entry = ttk.Entry(frame, font=("Helvetica", 10))
    apellido_entry.pack(fill="x", pady=5)

    # Dirección
    ttk.Label(frame, text="Dirección:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    direccion_entry = ttk.Entry(frame, font=("Helvetica", 10))
    direccion_entry.pack(fill="x", pady=5)

    # Teléfono
    ttk.Label(frame, text="Teléfono:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    telefono_entry = ttk.Entry(frame, font=("Helvetica", 10))
    telefono_entry.pack(fill="x", pady=5)

    # Email
    ttk.Label(frame, text="Email:", font=("Helvetica", 10)).pack(anchor="w", pady=(5, 0))
    email_entry = ttk.Entry(frame, font=("Helvetica", 10))
    email_entry.pack(fill="x", pady=5)

    def registrar_cliente():
        datos = {
            #"id_cliente": id_cliente_entry.get(),
            "nombre": nombre_entry.get(),
            "apellido": apellido_entry.get(),
            "direccion": direccion_entry.get(),
            "telefono": telefono_entry.get(),
            "email": email_entry.get()
        }
        # Validaciones
        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if "@" not in datos["email"]:
            messagebox.showerror("Error", "El email debe contener '@'.")
            return

        if any(char.isdigit() for char in datos["nombre"]):
            messagebox.showerror("Error", "El nombre no debe contener números.")
            return

        if any(char.isdigit() for char in datos["apellido"]):
            messagebox.showerror("Error", "El apellido no debe contener números.")
            return

        if any(char.isalpha() for char in datos["telefono"]):
            messagebox.showerror("Error", "El teléfono no debe contener letras.")
            return
        
        gestor_interfaces.registrar_cliente(datos["nombre"], datos["apellido"], datos["direccion"], datos["telefono"], datos["email"], ventana)

    # Botón para registrar cliente
    registrar_btn = ttk.Button(frame, text="Registrar", command=registrar_cliente)
    registrar_btn.pack(pady=10)

    # Aplicar estilo al botón
    registrar_btn.configure(style="TButton")
    estilo = ttk.Style()
    estilo.configure("TButton", font=("Helvetica", 10, "bold"), foreground="#000000", background="#4caf50")

def ventana_ver_clientes(root, clientes):
    ventana = tk.Toplevel(root)
    ventana.title("Lista de Clientes")
    ventana.geometry("900x400")

    # Título estilizado
    titulo = ttk.Label(ventana, text="Listado de Clientes", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=(10, 5))

    # Crear un marco para la tabla con borde y padding
    frame = ttk.Frame(ventana, padding=10, relief="solid", borderwidth=1)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Estilos para Treeview
    estilo = ttk.Style()
    estilo.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    estilo.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#b1dfe0", foreground="black")
    estilo.map("Treeview", background=[("selected", "#347083")], foreground=[("selected", "black")])

    # Crear el widget Treeview
    columnas = ("nombre", "apellido", "direccion", "telefono", "email")
    tree = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
    tree.pack(fill="both", expand=True)

    # Definir encabezados de columna
    tree.heading("nombre", text="Nombre")
    tree.heading("apellido", text="Apellido")
    tree.heading("direccion", text="Dirección")
    tree.heading("telefono", text="Teléfono")
    tree.heading("email", text="Email")

    # Ajustar el ancho de las columnas
    tree.column("nombre", width=120, anchor="center")
    tree.column("apellido", width=120, anchor="center")
    tree.column("direccion", width=200, anchor="center")
    tree.column("telefono", width=100, anchor="center")
    tree.column("email", width=150, anchor="center")

    # Alternar el color de fondo de las filas
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar datos a la tabla
    for i, cliente in enumerate(clientes):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=(cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]), tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    h_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=h_scrollbar.set)
    h_scrollbar.pack(side="bottom", fill="x")

# Asegúrate de cerrar la conexión a la base de datos al finalizar



