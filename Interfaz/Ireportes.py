import tkinter as tk
from tkinter import ttk, messagebox
from Reportes.gestorReportes import GestorReportes
from tkcalendar import DateEntry
from datetime import datetime

def ventana_reportes(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Reportes")
    ventana.geometry("400x400")

    gestor_reportes = GestorReportes(db)

    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana_reportes(ventana))

    # Crear un estilo para los botones
    estilo_boton = ttk.Style()
    estilo_boton.configure("TButton", padding=10, width=30)

    # Botón para Reporte 1 - Reservas
    boton_reporte1 = ttk.Button(ventana, text="Reporte de Reservas",
                                command=lambda: ventana_filtro_reservas(gestor_reportes),
                                style="TButton")
    boton_reporte1.pack(pady=10)

    # Botón para Reporte 2 - Ingresos
    boton_reporte2 = ttk.Button(ventana, text="Reporte de Ingresos",
                                command=lambda: ventana_filtro_mes(gestor_reportes.generar_reporte_ingresos, "Ingresos"),
                                style="TButton")
    boton_reporte2.pack(pady=10)

    # Botón para Reporte 3 - Ocupación
    boton_reporte3 = ttk.Button(ventana, text="Reporte de Ocupación",
                                command=lambda: ventana_filtro_mes(gestor_reportes.generar_reporte_ocupacion, "Ocupación"),
                                style="TButton")
    boton_reporte3.pack(pady=10)

    # Opcional: botones de gráficos con el mismo estilo
    boton_graficar_ingresos = ttk.Button(ventana, text="Graficar Ingresos Mensuales",
                                          command=lambda: gestor_reportes.graficar_ingresos_mensuales(),
                                          style="TButton")
    boton_graficar_ingresos.pack(pady=10)

    boton_graficar_ocupacion = ttk.Button(ventana, text="Graficar Ocupación Promedio",
                                           command=lambda: gestor_reportes.graficar_ocupacion_promedio(),
                                           style="TButton")
    boton_graficar_ocupacion.pack(pady=10)

def cerrar_ventana_reportes(ventana):
    ventana.destroy()

def ventana_filtro_reservas(gestor_reportes):
    ventana_filtro = tk.Toplevel()
    ventana_filtro.title("Filtrar Reservas")
    ventana_filtro.geometry("400x200")

    frame_fechas = ttk.Frame(ventana_filtro)
    frame_fechas.pack(pady=10)

    ttk.Label(frame_fechas, text="Fecha desde:").pack(side="left", padx=5)
    date_entry_desde = DateEntry(frame_fechas, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='d/m/y')
    date_entry_desde.pack(side="left", padx=5)

    ttk.Label(frame_fechas, text="Fecha hasta:").pack(side="left", padx=5)
    date_entry_hasta = DateEntry(frame_fechas, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='d/m/y')
    date_entry_hasta.pack(side="left", padx=5)

    boton_filtrar = ttk.Button(ventana_filtro, text="Filtrar",
                               command=lambda: mostrar_reporte_reservas("Reservas",
                                                                        gestor_reportes.generar_reporte_reservas(
                                                                            date_entry_desde.get_date().strftime('%Y-%m-%d'), 
                                                                            date_entry_hasta.get_date().strftime('%Y-%m-%d'))))
    boton_filtrar.pack(pady=10)

def ventana_filtro_mes(funcion_reporte, titulo):
    ventana_filtro = tk.Toplevel()
    ventana_filtro.title(f"Filtrar {titulo}")
    ventana_filtro.geometry("400x200")

    ttk.Label(ventana_filtro, text="Seleccione el mes:").pack(pady=5)
    date_entry_mes = DateEntry(ventana_filtro, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='d/m/y', year=datetime.now().year, month=datetime.now().month, day=1)
    date_entry_mes.pack(pady=5)

    boton_filtrar = ttk.Button(ventana_filtro, text="Filtrar",
                               command=lambda: mostrar_reporte_tabla(titulo, funcion_reporte(date_entry_mes.get_date().strftime('%Y-%m'))))
    boton_filtrar.pack(pady=10)

def mostrar_reporte(titulo, datos):
    # Convertir datos a texto
    datos_texto = "\n".join(str(item) for item in datos)
    messagebox.showinfo(f"Reporte de {titulo}", datos_texto)

def mostrar_reporte_tabla(titulo, datos):
    # Crear una nueva ventana para el reporte en formato tabla
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(f"Reporte de {titulo}")
    ventana_tabla.geometry("800x400")

    # Crear el Treeview para mostrar los datos en formato tabla
    tree = ttk.Treeview(ventana_tabla, show="headings")
    tree.pack(fill="both", expand=True)

    # Determinar las columnas de acuerdo a los datos (asumimos que cada entrada en datos es una lista o tupla)
    if not datos:
        messagebox.showinfo("Sin datos", f"No hay datos disponibles para el reporte de {titulo}.")
        return

    # Definir los encabezados específicos para cada tipo de reporte
    if titulo == "Ingresos":
        columnas = ["Nro Habitacion", "Tipo Habitacion", "Precio por noche"]
    elif titulo == "Ocupación":
        columnas = ["Tipo Habitacion", "Ocupación Promedio"]
    else:
        columnas = [f"Columna {i+1}" for i in range(len(datos[0]))]

    tree["columns"] = columnas

    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Alternar colores de fondo en filas
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar los datos a la tabla
    for i, fila in enumerate(datos):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=fila, tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar_y = ttk.Scrollbar(ventana_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    scrollbar_x = ttk.Scrollbar(ventana_tabla, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=scrollbar_x.set)
    scrollbar_x.pack(side="bottom", fill="x")

def mostrar_reporte_reservas(titulo, datos):
    # Crear una nueva ventana para el reporte en formato tabla
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(f"Reporte de {titulo}")
    ventana_tabla.geometry("800x400")

    # Crear el Treeview para mostrar los datos en formato tabla
    tree = ttk.Treeview(ventana_tabla, show="headings")
    tree.pack(fill="both", expand=True)

    # Verificar que hay datos y que son objetos con atributos
    if not datos:
        messagebox.showinfo("Sin datos", f"No hay datos disponibles para el reporte de {titulo}.")
        return

    # Obtener los nombres de los atributos del primer objeto como nombres de columnas, excluyendo 'id_reserva'
    columnas = [attr for attr in vars(datos[0]).keys() if attr != 'id_reserva']
    tree["columns"] = columnas

    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col.replace('_', ' ').capitalize())
        tree.column(col, anchor="center", width=100)

    # Alternar colores de fondo en filas
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar los datos a la tabla
    for i, obj in enumerate(datos):
        # Obtener los valores de cada atributo del objeto, excluyendo 'id_reserva'
        fila = [getattr(obj, attr) for attr in columnas]
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=fila, tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar_y = ttk.Scrollbar(ventana_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    scrollbar_x = ttk.Scrollbar(ventana_tabla, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=scrollbar_x.set)
    scrollbar_x.pack(side="bottom", fill="x")

def mostrar_reporte_ingresos(titulo, datos):
    # Crear una nueva ventana para el reporte en formato tabla
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(f"Reporte de {titulo}")
    ventana_tabla.geometry("800x400")

    # Crear el Treeview para mostrar los datos en formato tabla
    tree = ttk.Treeview(ventana_tabla, show="headings")
    tree.pack(fill="both", expand=True)

    # Verificar que hay datos
    if not datos:
        messagebox.showinfo("Sin datos", f"No hay datos disponibles para el reporte de {titulo}.")
        return

    # Definir las columnas
    columnas = ["Nro Habitacion", "Tipo Habitacion", "Precio por noche"]
    tree["columns"] = columnas

    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Alternar colores de fondo en filas
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar los datos a la tabla
    for i, fila in enumerate(datos):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=fila, tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar_y = ttk.Scrollbar(ventana_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    scrollbar_x = ttk.Scrollbar(ventana_tabla, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=scrollbar_x.set)
    scrollbar_x.pack(side="bottom", fill="x")

def mostrar_reporte_ocupacion(titulo, datos):
    # Crear una nueva ventana para el reporte en formato tabla
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(f"Reporte de {titulo}")
    ventana_tabla.geometry("800x400")

    # Crear el Treeview para mostrar los datos en formato tabla
    tree = ttk.Treeview(ventana_tabla, show="headings")
    tree.pack(fill="both", expand=True)

    # Verificar que hay datos
    if not datos:
        messagebox.showinfo("Sin datos", f"No hay datos disponibles para el reporte de {titulo}.")
        return

    # Definir las columnas
    columnas = ["Tipo Habitacion", "Ocupación Promedio"]
    tree["columns"] = columnas

    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Alternar colores de fondo en filas
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar los datos a la tabla
    for i, fila in enumerate(datos):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values = fila, tags=(tag,))

    # Barra de desplazamiento vertical
    scrollbar_y = ttk.Scrollbar(ventana_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")

    # Barra de desplazamiento horizontal
    scrollbar_x = ttk.Scrollbar(ventana_tabla, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=scrollbar_x.set)
    scrollbar_x.pack(side="bottom", fill="x")