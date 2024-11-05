import tkinter as tk
from tkinter import ttk, messagebox
from Reportes.gestorReportes import GestorReportes

def ventana_reportes(root, db):
    ventana = tk.Toplevel(root)
    ventana.title("Reportes")
    ventana.geometry("700x600")

    gestor_reportes = GestorReportes(db)

    fecha_inicio = "2024-03-01"  # Podrías hacer que estas fechas sean dinámicas con inputs
    fecha_fin = "2024-03-31"

    # Botón para Reporte 1 - Reservas
    boton_reporte1 = ttk.Button(ventana, text="Reporte de Reservas", 
                                command=lambda: mostrar_reporte_tabla2("Reservas", gestor_reportes.generar_reporte_reservas(fecha_inicio, fecha_fin)))
    boton_reporte1.pack(pady=10)

    # Botón para Reporte 2 - Ingresos
    boton_reporte2 = ttk.Button(ventana, text="Reporte de Ingresos", 
                                command=lambda: mostrar_reporte("Ingresos", gestor_reportes.generar_reporte_ingresos()))
    boton_reporte2.pack(pady=10)

    # Botón para Reporte 3 - Ocupación
    boton_reporte3 = ttk.Button(ventana, text="Reporte de Ocupación", 
                                command=lambda: mostrar_reporte("Ocupación", gestor_reportes.generar_reporte_ocupacion()))
    boton_reporte3.pack(pady=10)

    # Opcional: botones de gráficos con el mismo estilo
    boton_graficar_ingresos = ttk.Button(ventana, text="Graficar Ingresos Mensuales", command=gestor_reportes.graficar_ingresos_mensuales, style="TButton")
    boton_graficar_ingresos.pack(pady=10, padx=20, fill="x")

    boton_graficar_ocupacion = ttk.Button(ventana, text="Graficar Ocupación Promedio", command=gestor_reportes.graficar_ocupacion_promedio, style="TButton")
    boton_graficar_ocupacion.pack(pady=10, padx=20, fill="x")

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

    columnas = [f"Columna {i+1}" for i in range(len(datos[0]))]
    tree["columns"] = columnas

    # Configurar encabezados
    for i, col in enumerate(columnas):
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

def mostrar_reporte_tabla2(titulo, datos):
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

    # Obtener los nombres de los atributos del primer objeto como nombres de columnas
    columnas = [attr for attr in vars(datos[0]).keys()]
    tree["columns"] = columnas

    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col.capitalize())
        tree.column(col, anchor="center", width=100)

    # Alternar colores de fondo en filas
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=25)
    estilo.map("Treeview", background=[("selected", "#b1dfe0")], foreground=[("selected", "black")])
    tree.tag_configure("oddrow", background="#f2f2f2")
    tree.tag_configure("evenrow", background="#ffffff")

    # Agregar los datos a la tabla
    for i, obj in enumerate(datos):
        # Obtener los valores de cada atributo del objeto y convertirlos en una lista
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