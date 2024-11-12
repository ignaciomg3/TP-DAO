import tkinter as tk
from tkinter import ttk, messagebox
from Reportes.gestorReportes import GestorReportes
from tkcalendar import DateEntry
from datetime import datetime


def configurar_estilo_treeview():
    """Configura el estilo de filas alternadas y seleccionadas en el Treeview."""
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
    return estilo


def crear_treeview(ventana_tabla, columnas):
    tree = ttk.Treeview(ventana_tabla, columns=columnas, show="headings", style="Treeview")
    tree.pack(expand=True, fill="both")
    for col in columnas:
        tree.heading(col, text=col)
    return tree


def insertar_datos_treeview(tree, datos):
    for i, dato in enumerate(datos):
        tree.insert("", "end", values=dato, tags=("oddrow" if i % 2 == 0 else "evenrow"))
    tree.tag_configure("oddrow", background="white")
    tree.tag_configure("evenrow", background="lightgrey")


def mostrar_tabla_Igna(ventana_tabla, estilo):
    columnas = ("col1", "col2", "col3")
    tree = crear_treeview(ventana_tabla, columnas)
    datos = [("Dato 1", "Dato 2", "Dato 3"),
             ("Dato 4", "Dato 5", "Dato 6"),
             ("Dato 7", "Dato 8", "Dato 9")]
    insertar_datos_treeview(tree, datos)


def crear_filtro_fecha(filtro_frame, label_text):
    ttk.Label(filtro_frame, text=label_text).pack(side="left", padx=5)
    date_entry = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry.pack(side="left", padx=5)
    return date_entry

def mostrar_filtros_fechas(ventana_tabla):
    filtro_frame = ttk.Frame(ventana_tabla)
    filtro_frame.pack(pady=10)
    date_entry_desde = crear_filtro_fecha(filtro_frame, "Fecha desde:")
    date_entry_hasta = crear_filtro_fecha(filtro_frame, "Fecha hasta:")
    boton_filtrar = ttk.Button(filtro_frame, text="Filtrar", command=lambda: None)
    boton_filtrar.pack(side="left", padx=5)
    obtener_estilo = configurar_estilo_treeview()
    #mostrar_tabla_Igna(ventana_tabla, obtener_estilo)
    return date_entry_desde, date_entry_hasta


def crear_boton_reporte(ventana, texto, comando):
    boton = ttk.Button(ventana, text=texto, command=comando)
    boton.pack(pady=10)
    return boton


def ventana_reportes2(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Reportes")
    ventana.geometry("700x600")
    gestor_reportes = GestorReportes(db)
    date_entry_desde, date_entry_hasta = mostrar_filtros_fechas(ventana)
    
    def obtener_fechas_y_mostrar_reporte():
        fecha_inicio = date_entry_desde.get_date().strftime('%Y-%m-%d')
        fecha_fin = date_entry_hasta.get_date().strftime('%Y-%m-%d')
        mostrar_reporte_reservas("Reservas", gestor_reportes.generar_reporte_reservas(fecha_inicio, fecha_fin))

    crear_boton_reporte(ventana, "Reporte de Reservas", obtener_fechas_y_mostrar_reporte)
    crear_boton_reporte(ventana, "Reporte de Ingresos",
                        lambda: mostrar_reporte("Ingresos",
                                                gestor_reportes.generar_reporte_ingresos()))
    crear_boton_reporte(ventana, "Reporte de Ocupación",
                        lambda: mostrar_reporte("Ocupación",
                                                gestor_reportes.generar_reporte_ocupacion()))
    crear_boton_reporte(ventana, "Graficar Ingresos Mensuales",
                        gestor_reportes.graficar_ingresos_mensuales)
    crear_boton_reporte(ventana, "Graficar Ocupación Promedio",
                        gestor_reportes.graficar_ocupacion_promedio)


def mostrar_reporte(titulo, datos):
    datos_texto = "\n".join(str(item) for item in datos)
    messagebox.showinfo(f"Reporte de {titulo}", datos_texto)


def mostrar_reporte_tabla(titulo, datos):
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(f"Reporte de {titulo}")
    ventana_tabla.geometry("800x400")
    tree = ttk.Treeview(ventana_tabla, show="headings")
    tree.pack(fill="both", expand=True)
    if not datos:
        messagebox.showinfo("Sin datos", f"No hay datos disponibles para el reporte de {titulo}.")
        return
    columnas = [f"Columna {i+1}" for i in range(len(datos[0]))]
    tree["columns"] = columnas
    for i, col in enumerate(columnas):
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)
    estilo = configurar_estilo_treeview()
    insertar_datos_treeview(tree, datos)
    scrollbar_y = ttk.Scrollbar(ventana_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar_y.set)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x = ttk.Scrollbar(ventana_tabla, orient="horizontal", command=tree.xview)
    tree.configure(xscroll=scrollbar_x.set)
    scrollbar_x.pack(side="bottom", fill="x")


def mostrar_reporte_reservas(titulo, datos):
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(f"Reporte de {titulo}")
    ventana_tabla.geometry("800x400")
    filtro_frame = ttk.Frame(ventana_tabla)
    filtro_frame.pack(pady=10)
    date_entry_desde = crear_filtro_fecha(filtro_frame, "Fecha desde:")
    date_entry_hasta = crear_filtro_fecha(filtro_frame, "Fecha hasta:")
    boton_filtrar = ttk.Button(filtro_frame, text="Filtrar",
                               command=lambda: filtrar_reservas_por_fecha(date_entry_desde.get_date(),
                                                                         date_entry_hasta.get_date(), tree, datos))
    boton_filtrar.pack(pady=5)
    tree = ttk.Treeview(ventana_tabla, show="headings")
    tree.pack(fill="both", expand=True)
    # if not datos:
    #     messagebox.showinfo("Sin datos", f"No hay datos disponibles para el reporte de {titulo}.")
    #     return
    # columnas = [attr for attr in vars(datos[0]).keys()]
    # tree["columns"] = columnas
    # for col in columnas:
    #     tree.heading(col, text=col.capitalize())
    #     tree.column(col, anchor="center", width=100)
    # estilo = configurar_estilo_treeview()
    # insertar_datos_treeview(tree, datos)
    # scrollbar_y = ttk.Scrollbar(ventana_tabla, orient="vertical", command=tree.yview)
    # tree.configure(yscroll=scrollbar_y.set)
    # scrollbar_y.pack(side="right", fill="y")
    # scrollbar_x = ttk.Scrollbar(ventana_tabla, orient="horizontal", command=tree.xview)
    # tree.configure(xscroll=scrollbar_x.set)
    # scrollbar_x.pack(side="bottom", fill="x")


def filtrar_reservas_por_fecha(fecha_desde, fecha_hasta, tree, datos):
    reservas_filtradas = [reserva for reserva in datos if fecha_desde <= reserva.fecha_entrada <= fecha_hasta]
    for item in tree.get_children():
        tree.delete(item)
    for i, reserva in enumerate(reservas_filtradas):
        fila = [getattr(reserva, attr) for attr in vars(reserva).keys()]
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", "end", values=fila, tags=(tag,))
