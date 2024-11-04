from Datos.gestor_db import GestorDB

def verificar_superposicion_reserva(numero_habitacion, fecha_entrada, fecha_salida):
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT COUNT(*) FROM Reserva 
        WHERE numero_habitacion = ? AND 
        ((fecha_entrada <= ? AND fecha_salida >= ?) OR 
        (fecha_entrada >= ? AND fecha_salida <= ?))
    '''
    cursor = gestor.ejecutar_consulta(consulta, (numero_habitacion, fecha_salida, fecha_entrada, fecha_entrada, fecha_salida))
    superposiciones = cursor.fetchone()[0] if cursor else 0
    gestor.desconectar()
    return superposiciones == 0

def validar_empleado_asignaciones(id_empleado, fecha):
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT COUNT(*)
        FROM Reserva R
        JOIN Empleado E ON R.id_empleado = E.id_empleado
        WHERE E.id_empleado = ? AND DATE(R.fecha_entrada) = ?
    '''
    cursor = gestor.ejecutar_consulta(consulta, (id_empleado, fecha))
    asignaciones= cursor.fetchone()[0] >= 5 if cursor else 0
    gestor.desconectar()
    return asignaciones == 0

