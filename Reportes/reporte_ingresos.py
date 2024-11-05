from Datos.gestor_db import GestorDB

def generar_reporte_ingresos():  # sourcery skip: use-named-expression
    gestor_db = GestorDB()
    ingresos_por_habitacion = []

    try:
        gestor_db.conectar()
        
        consulta = '''
            SELECT H.numero, SUM(F.total) as total_ingresos
            FROM facturas F
            JOIN reservas R ON F.id_reserva = R.id_reserva
            JOIN habitaciones H ON R.numero_habitacion = H.numero
            GROUP BY H.numero
            ORDER BY H.numero
        '''
        
        cursor = gestor_db.ejecutar_consulta(consulta)
        if cursor:
            for fila in cursor.fetchall():
                numero_habitacion, total_ingresos = fila
                ingresos_por_habitacion.append((numero_habitacion, total_ingresos))

    except Exception as e:
        print(f"Error al generar el reporte de ingresos por habitación: {e}")
    
    finally:
        gestor_db.desconectar()

    return ingresos_por_habitacion