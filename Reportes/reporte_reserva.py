from Datos.gestor_db import GestorDB
from Entidades.reserva import *
from datetime import datetime

def listar_reservas(fecha_inicio, fecha_fin):
    lista_reservas= []
    gestor = GestorDB()
    gestor.conectar()
    consulta = '''
        SELECT r.id_reserva, c.nombre || ' ' || c.apellido AS cliente, 
        r.numero_habitacion, r.fecha_entrada, r.fecha_salida, r.cantidad_personas
        FROM reservas r
        JOIN clientes c ON r.id_cliente = c.id_cliente
        WHERE r.fecha_entrada >= ? AND r.fecha_salida <= ?
    '''
    cursor = gestor.ejecutar_consulta(consulta, (fecha_inicio, fecha_fin))
    
    reservas = cursor.fetchall() if cursor else []
    for r in reservas:
        fecha_entrada = datetime.strptime(r[3], '%Y-%m-%d').strftime('%d/%m/%Y')
        fecha_salida = datetime.strptime(r[4], '%Y-%m-%d').strftime('%d/%m/%Y')
        reserva = Reserva(
            id_reserva = r[0],
            cliente= r[1],
            habitacion= r[2],
            fecha_entrada= fecha_entrada,
            fecha_salida= fecha_salida,
            cantidad_personas= r[5],
        )
            
        lista_reservas.append(reserva)
                
    gestor.desconectar()
    return lista_reservas