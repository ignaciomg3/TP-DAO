from Datos.gestor_db import GestorDB
from Reportes.validaciones import verificar_superposicion_reserva

def listar_reservas(fecha_inicio, fecha_fin):
    lista_reservas= []
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT * FROM Reserva 
        WHERE fecha_entrada >= ? AND fecha_salida <= ?
    '''
    cursor = gestor.ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))
    
    reservas = cursor.fetchall() if cursor else []
    for r in reservas:
        numero_habitacion = r[2]
        fecha_entrada = r[3]  
        fecha_salida = r[4] 
        if verificar_superposicion_reserva(numero_habitacion, fecha_entrada, fecha_salida):
            lista_reservas.append(r)
            
    gestor.desconectar()
    return lista_reservas