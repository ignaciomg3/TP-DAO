import matplotlib.pyplot as plt
from Datos.gestor_db import GestorDB

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
    consulta = '''
        SELECT strftime('%Y-%m', fecha_emision) as mes, SUM(total) as total
        FROM Factura
        GROUP BY mes
    '''
    cursor = gestor.ejecutar_consulta(consulta)
    datos = cursor.fetchall() if cursor else []
    meses = [dato[0] for dato in datos]
    ingresos = [dato[1] for dato in datos]

    plt.plot(meses, ingresos)
    plt.xlabel('Mes')
    plt.ylabel('Ingresos Totales')
    plt.title('Ingresos Mensuales')
    plt.show()