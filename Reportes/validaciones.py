from Datos.gestor_db import GestorDB

def verificar_superposicion_reserva(gestor, numero_habitacion, fecha_entrada, fecha_salida):
    #gestor = GestorDB()
    #gestor.conectar()
    consulta = '''
        SELECT COUNT(*) FROM reservas 
        WHERE numero_habitacion = ? AND 
        ((fecha_entrada <= ? AND fecha_salida >= ?) OR 
        (fecha_entrada >= ? AND fecha_salida <= ?))
    '''
    cursor = gestor.ejecutar_consulta(consulta, (numero_habitacion, fecha_salida, fecha_entrada, fecha_entrada, fecha_salida))
    superposiciones = cursor.fetchone()[0] if cursor else 0
    #gestor.desconectar()
    return superposiciones == 0


