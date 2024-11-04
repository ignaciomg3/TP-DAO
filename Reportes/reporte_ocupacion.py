from Datos.gestor_db import GestorDB

def reporte_ocupacion_promedio():
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
    ocupacion_promedio = cursor.fetchall() if cursor else []
    gestor.desconectar()
    return ocupacion_promedio