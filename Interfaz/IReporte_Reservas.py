import tkinter as tk
from tkinter import ttk, messagebox
#from ..Reportes.gestorReportes import GestorReportes
from tkcalendar import DateEntry

class ReporteReservas:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Reportes")
        self.ventana.geometry("700x600")
        self.estilo = self.configurar_estilo_treeview()
        self.mostrar_filtros_fechas()
        self.mostrar_tabla()

    def mostrar_filtros_fechas(self):
        # Selección de fecha
        filtro_frame = ttk.Frame(self.ventana)
        filtro_frame.pack(pady=10)

        ttk.Label(filtro_frame, text="Ingrese una fecha:").pack(side="left", padx=5)
        date_entry = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)

        # Label y DateEntry para seleccionar la fecha desde
        label_fecha_desde = ttk.Label(filtro_frame, text="Fecha desde:")
        label_fecha_desde.pack(side="left", padx=5)
        date_entry_desde = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_entry_desde.pack(side="left", padx=5)

        # Label y DateEntry para seleccionar la fecha hasta
        label_fecha_hasta = ttk.Label(filtro_frame, text="Fecha hasta:")
        label_fecha_hasta.pack(side="left", padx=5)
        date_entry_hasta = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_entry_hasta.pack(side="left", padx=5)

        # Botón para filtrar las reservas por rango de fechas
        boton_filtrar = ttk.Button(filtro_frame, text="Filtrar", command=lambda: None)
        boton_filtrar.pack(side="left", padx=5)

    def configurar_estilo_treeview(self):
        """Configura el estilo de filas alternadas y seleccionadas en el Treeview."""
        estilo = ttk.Style()
        estilo.configure("Treeview", rowheight=25)
        estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
        return estilo

    def mostrar_tabla(self):
        # Crear un Treeview con filas de colores alternados
        columnas = ("col1", "col2", "col3")
        tree = ttk.Treeview(self.ventana, columns=columnas, show="headings", style="Treeview")
        tree.pack(expand=True, fill="both")

        # Definir encabezados de columna
        for col in columnas:
            tree.heading(col, text=col)

        # Insertar datos de ejemplo en la tabla
        datos = [("Dato 1", "Dato 2", "Dato 3"),
                 ("Dato 4", "Dato 5", "Dato 6"),
                 ("Dato 7", "Dato 8", "Dato 9")]

        for i, dato in enumerate(datos):
            tree.insert("", "end", values=dato, tags=("oddrow" if i % 2 == 0 else "evenrow"))

        # Configurar colores alternados
        tree.tag_configure("oddrow", background="white")
        tree.tag_configure("evenrow", background="lightgrey")


def mostrar_filtros_fechas(ventana_tabla):
      # Selección de fecha
    filtro_frame = ttk.Frame(ventana_tabla)
    filtro_frame.pack(pady=10)

    ttk.Label(filtro_frame, text="Ingrese una fecha:").pack(side="left", padx=5)
    date_entry = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)

    # Label y DateEntry para seleccionar la fecha desde
    label_fecha_desde = ttk.Label(filtro_frame, text="Fecha desde:")
    label_fecha_desde.pack(side="left", padx=5)
    date_entry_desde = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry_desde.pack(side="left", padx=5)

    # Label y DateEntry para seleccionar la fecha hasta
    label_fecha_hasta = ttk.Label(filtro_frame, text="Fecha hasta:")
    label_fecha_hasta.pack(side="left", padx=5)
    date_entry_hasta = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry_hasta.pack(side="left", padx=5)

    # Botón para filtrar las reservas por rango de fechas
    boton_filtrar = ttk.Button(filtro_frame, text="Filtrar", command=lambda: None)
    boton_filtrar.pack(side="left", padx=5)

def configurar_estilo_treeview():
        """Configura el estilo de filas alternadas y seleccionadas en el Treeview."""
        estilo = ttk.Style()
        estilo.configure("Treeview", rowheight=25)  
        estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
        return estilo

def mostrar_tabla(ventana_tabla, estilo):
    # Crear un Treeview con filas de colores alternados
    columnas = ("col1", "col2", "col3")
    tree = ttk.Treeview(ventana_tabla, columns=columnas, show="headings", style="Treeview")
    tree.pack(expand=True, fill="both")

    # Definir encabezados de columna
    for col in columnas:
        tree.heading(col, text=col)

    # Insertar datos de ejemplo en la tabla
    datos = [("Dato 1", "Dato 2", "Dato 3"),
            ("Dato 4", "Dato 5", "Dato 6"),
            ("Dato 7", "Dato 8", "Dato 9")]

    for i, dato in enumerate(datos):
        tree.insert("", "end", values=dato, tags=("oddrow" if i % 2 == 0 else "evenrow"))

    # Configurar colores alternados
    tree.tag_configure("oddrow", background="white")
    tree.tag_configure("evenrow", background="lightgrey")

def ventana_reportes(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Reportes")
    ventana.geometry("700x600")

    #gestor_reportes = GestorReportes(db)

    mostrar_filtros_fechas(ventana)
    estilo = configurar_estilo_treeview()
    mostrar_tabla(ventana, estilo)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    ventana_reportes(root, None)
    root.mainloop()
    
