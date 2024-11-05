import tkinter as tk
from tkinter import ttk, messagebox
from Datos.gestor_db import GestorDB
from Entidades.cliente import Cliente


def ventana_registrar_cliente(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Registrar Cliente")

    # Campos de entrada
    ttk.Label(ventana, text="ID de Cliente:").pack()
    id_cliente_entry = ttk.Entry(ventana)
    id_cliente_entry.pack()

    ttk.Label(ventana, text=" Nombre :").pack()
    nombre_entry = ttk.Entry(ventana)
    nombre_entry.pack()

    ttk.Label(ventana, text="Apellido:").pack()
    apellido_entry = ttk.Entry(ventana)
    apellido_entry.pack()

    ttk.Label(ventana, text="Dirección:").pack()
    direccion_entry = ttk.Entry(ventana)
    direccion_entry.pack()

    ttk.Label(ventana, text="Telefono:").pack()
    telefono_entry = ttk.Entry(ventana)
    telefono_entry.pack()

    ttk.Label(ventana, text="Email:").pack()
    email_entry = ttk.Entry(ventana)
    email_entry.pack()

    # Botón para registrar CLIENTE
    ttk.Button(ventana, text="Registrar", command=lambda: registrar_cliente(
        id_cliente_entry.get(), nombre_entry.get(), apellido_entry.get(), direccion_entry.get(), telefono_entry.get(), email_entry.get(), ventana, db
    )).pack(pady=10)

def registrar_cliente(id_cliente, nombre, apellido, direccion, telefono, email, ventana, db):
    try:
        db.insertar_cliente(id_cliente, nombre, apellido, direccion, telefono, email)
        messagebox.showinfo("Registro Exitoso", f"Cliente {nombre} {apellido} registrado con éxito.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")

def ventana_ver_clientes(root, db):
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
    columnas = ("id", "nombre", "apellido", "direccion", "telefono", "email")
    tree = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
    tree.pack(fill="both", expand=True)

    # Definir encabezados de columna
    tree.heading("id", text="ID")
    tree.heading("nombre", text="Nombre")
    tree.heading("apellido", text="Apellido")
    tree.heading("direccion", text="Dirección")
    tree.heading("telefono", text="Teléfono")
    tree.heading("email", text="Email")

    # Ajustar el ancho de las columnas
    tree.column("id", width=50, anchor="center")
    tree.column("nombre", width=120, anchor="center")
    tree.column("apellido", width=120, anchor="center")
    tree.column("direccion", width=200, anchor="center")
    tree.column("telefono", width=100, anchor="center")
    tree.column("email", width=150, anchor="center")

    # Alternar el color de fondo de las filas
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar datos a la tabla
    clientes = db.obtener_clientes()
    for i, cliente in enumerate(clientes):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=cliente, tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    h_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=h_scrollbar.set)
    h_scrollbar.pack(side="bottom", fill="x")

# Asegúrate de cerrar la conexión a la base de datos al finalizar