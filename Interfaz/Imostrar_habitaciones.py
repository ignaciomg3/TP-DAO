import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry

def ventana_ver_habitaciones(root, gestorI):
    def filtrar_habitaciones():
        fecha_seleccionada = date_entry.get_date().strftime('%Y-%m-%d')
        habitaciones_disponibles = gestorI.filtrar_habitaciones(fecha_seleccionada)
        
        for item in tree.get_children():
            tree.delete(item)
        
        for i, habitacion in enumerate(habitaciones_disponibles):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree.insert("", "end", values=habitacion, tags=(tag,))

    ventana = tk.Toplevel(root)
    ventana.title("Lista de Habitaciones")
    ventana.minsize(400, 500)
    ventana.geometry("900x600+0+0")
    
    # Título estilizado
    titulo = ttk.Label(ventana, text="Listado de Habitaciones Disponibles", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=(10, 5))

    # Selección de fecha
    filtro_frame = ttk.Frame(ventana)
    filtro_frame.pack(pady=10)
    
    ttk.Label(filtro_frame, text="Ingrese una fecha:").pack(side="left", padx=5)
    date_entry = DateEntry(
        filtro_frame, 
        width=12, 
        background='black', 
        foreground='white', 
        borderwidth=2, 
        date_pattern='dd/MM/yyyy',  # Mostrar fecha en formato d/m/y
        showweeknumbers=False,  # Ocultar números de semana
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
    date_entry.pack(side="left", padx=5)
    
    # Botón para filtrar habitaciones
    ttk.Button(filtro_frame, text="Filtrar", command=filtrar_habitaciones).pack(side="left", padx=5)

    # Crear un marco para la tabla con borde y padding
    frame = ttk.Frame(ventana, padding=10, relief="solid", borderwidth=1)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Estilos para Treeview
    estilo = ttk.Style()
    estilo.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    estilo.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#b1dfe0", foreground="black")
    estilo.map("Treeview", background=[("selected", "#b1dfe0")])

    # Alternar colores de fila
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])

    # Crear el widget Treeview
    columnas = ("numero", "tipo", "estado", "precio")
    tree = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
    tree.pack(fill="both", expand=True)

    # Definir encabezados de columna
    tree.heading("numero", text="Número de Habitación")
    tree.heading("tipo", text="Tipo")
    tree.heading("estado", text="Estado")
    tree.heading("precio", text="Precio por Noche")

    # Ajustar el ancho de las columnas
    tree.column("numero", width=120, anchor="center")
    tree.column("tipo", width=100, anchor="center")
    tree.column("estado", width=100, anchor="center")
    tree.column("precio", width=100, anchor="center")

    # Alternar el color de fondo de las filas
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    h_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=h_scrollbar.set)
    h_scrollbar.pack(side="bottom", fill="x")
    
    # Llamar a filtrar_habitaciones para mostrar todas las disponibles al abrir
    filtrar_habitaciones()
