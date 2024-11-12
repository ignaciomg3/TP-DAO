from Datos.gestor_db import GestorDB

def generar_reporte_ingresos(gestor_db, mes):
    ingresos_por_habitacion = []
    consulta = '''
        SELECT H.numero, H.tipo, SUM(F.total) as total_ingresos
        FROM facturas F
        JOIN reservas R ON F.id_reserva = R.id_reserva
        JOIN habitaciones H ON R.numero_habitacion = H.numero
        WHERE strftime('%Y-%m', R.fecha_entrada) = ?
        GROUP BY H.numero, H.tipo
        ORDER BY H.numero
    '''
    cursor = gestor_db.ejecutar_consulta(consulta, (mes,))
    if cursor:
        for fila in cursor.fetchall():
            numero_habitacion, tipo_habitacion, total_ingresos = fila
            ingresos_por_habitacion.append((numero_habitacion, tipo_habitacion, total_ingresos))
    return ingresos_por_habitacion