import matplotlib.pyplot as plt
from Datos.gestor_db import GestorDB
import sqlite3
from datetime import datetime
from time import sleep

def graficar_ocupacion_promedio():
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT tipo_habitacion, AVG(ocupacion) as ocupacion_promedio
        FROM (
            SELECT Habitacion.tipo, COUNT(Reserva.id_reserva) as ocupacion
            FROM Habitacion
            LEFT JOIN Reserva ON Habitacion.numero = Reserva.numero_habitacion
            GROUP BY Habitacion.tipo
        )
        GROUP BY tipo_habitacion
    '''
    cursor = gestor.ejecutar_consulta(consulta)
    datos = cursor.fetchall() if cursor else []
    tipos = [dato[0] for dato in datos]
    ocupaciones = [dato[1] for dato in datos]

    plt.bar(tipos, ocupaciones)
    plt.xlabel('Tipo de Habitación')
    plt.ylabel('Ocupación Promedio')
    plt.title('Ocupación Promedio por Tipo de Habitación')
    plt.show()

def graficar_ingresos_mensuales():
    gestor = GestorDB()
    gestor.conectar()
    # Consulta para obtener los ingresos mensuales
    sleep (1)
    consulta = '''
        SELECT strftime('%Y-%m', fecha_emision) AS mes, SUM(total) AS total_generado
        FROM facturas
            
            GROUP BY mes
            ORDER BY mes
    '''
    cursor = gestor.ejecutar_consulta(consulta, )
    datos = cursor.fetchall() if cursor else []

    # Crear un diccionario para los ingresos por mes
    ingresos_por_mes = {f"{year}-{month:02}": 0 for year in range(2024, 2025) for month in range(1, 13)}

    # Rellenar el diccionario con los ingresos obtenidos de la consulta
    for row in datos:
        ingresos_por_mes[row[0]] = row[1]

    # Extraer meses e ingresos totales
    meses = list(ingresos_por_mes.keys())
    ingresos = list(ingresos_por_mes.values())

    # Convertir los meses a un formato legible
    meses_legibles = [datetime.strptime(mes, '%Y-%m').strftime('%B %Y') for mes in meses]

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(meses_legibles, ingresos, marker='o')
    plt.title('Ingresos Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Total Ingresos')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()
    
    gestor.desconectar()

