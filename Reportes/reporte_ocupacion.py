from Datos.gestor_db import GestorDB

def reporte_ocupacion_promedio():
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT tipo, AVG(ocupacion) as ocupacion_promedio
        FROM (
            SELECT habitaciones.tipo, COUNT(reservas.id) as ocupacion
            FROM habitaciones
            LEFT JOIN reservas ON habitaciones.numero = reservas.numero_habitacion
            GROUP BY habitaciones.tipo
        )
        GROUP BY tipo
    '''
    cursor = gestor.ejecutar_consulta(consulta)
    ocupacion_promedio = cursor.fetchall() if cursor else []
    gestor.desconectar()
    return ocupacion_promedio