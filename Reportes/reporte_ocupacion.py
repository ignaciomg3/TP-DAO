from Datos.gestor_db import GestorDB

def reporte_ocupacion_promedio(mes):
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT tipo, AVG(ocupacion) as ocupacion_promedio
        FROM (
            SELECT habitaciones.tipo, COUNT(reservas.id_reserva) as ocupacion
            FROM habitaciones
            LEFT JOIN reservas ON habitaciones.numero = reservas.numero_habitacion
            WHERE strftime('%Y-%m', reservas.fecha_entrada) = ?
            GROUP BY habitaciones.tipo
        )
        GROUP BY tipo
    '''
    cursor = gestor.ejecutar_consulta(consulta, (mes,))
    ocupacion_promedio = cursor.fetchall() if cursor else []
    gestor.desconectar()
    return ocupacion_promedio