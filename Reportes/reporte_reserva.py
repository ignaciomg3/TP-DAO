from Datos.gestor_db import GestorDB
from Entidades.reserva import *

def listar_reservas(fecha_inicio, fecha_fin):
    lista_reservas= []
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT * FROM reservas 
        WHERE fecha_entrada >= ? AND fecha_salida <= ?
    '''
    cursor = gestor.ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))
    
    reservas = cursor.fetchall() if cursor else []
    for r in reservas:
            reserva = Reserva(
                id_reserva = r[0],
                cliente= r[1],
                habitacion= r[2],
                fecha_entrada= r[3],
                fecha_salida= r[4],
                cantidad_personas= r[5],
            )
            
            lista_reservas.append(reserva)
                
    gestor.desconectar()
    return lista_reservas