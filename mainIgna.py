from Datos.gestor_db import GestorDB
from time import sleep

def main():
    

    ## gestorBaseDatos.crear_tablas()
    ##rellenar tablas

    
    while True:
        print("\n********** Menú del Sistema de Gestión de Hotel **********")
        print("1. Registrar una nueva habitación")
        print("2. Registrar un nuevo cliente")
        print("3. Realizar una reserva")
        print("4. Generar una factura")
        print("5. Registrar un empleado")
        print("6. Crear la base de datos y rellenarla con datos de ejemplo")
        print("7. Mostrar Tablas")
        #eliminar una habitacion
        print("8. Eliminar una habitacion")
        print("15. Salir del sistema")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Ejemplo de registro de una habitación
            numero = int(input("Número de habitación: "))
            tipo = input("Tipo de habitación (simple, doble, suite): ")
            estado = input("Estado de la habitación (disponible/ocupada): ")
            precio_por_noche = float(input("Precio por noche: "))
            gestorBaseDatos.conectar()
            gestorBaseDatos.insertar_habitacion(numero, tipo, estado, precio_por_noche)
            gestorBaseDatos.desconectar()

        elif opcion == "2":
            # Ejemplo de registro de un cliente
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            direccion = input("Dirección del cliente: ")
            telefono = input("Teléfono del cliente: ")
            email = input("Email del cliente: ")
            gestorBaseDatos.conectar()
            gestorBaseDatos.insertar_cliente(id_cliente, nombre, apellido, direccion, telefono, email)
            gestorBaseDatos.desconectar()

        elif opcion == "3":
            # Ejemplo de realizar una reserva
            id_reserva = int(input("ID de la reserva: "))
            id_cliente = int(input("ID del cliente: "))
            numero_habitacion = int(input("Número de la habitación: "))
            fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
            fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")
            cantidad_personas = int(input("Cantidad de personas: "))
            gestorBaseDatos.conectar()
            gestorBaseDatos.insertar_reserva(id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas)
            gestorBaseDatos.desconectar()

        elif opcion == "4":
            # Ejemplo de generación de una factura
            id_factura = int(input("ID de la factura: "))
            id_cliente = int(input("ID del cliente: "))
            id_reserva = int(input("ID de la reserva: "))
            fecha_emision = input("Fecha de emisión (YYYY-MM-DD): ")
            total = float(input("Total a pagar: "))
            gestorBaseDatos.conectar()
            gestorBaseDatos.insertar_factura(id_factura, id_cliente, id_reserva, fecha_emision, total)
            gestorBaseDatos.desconectar()

        elif opcion == "5":
            # Ejemplo de registro de un empleado
            id_empleado = int(input("ID del empleado: "))
            nombre = input("Nombre del empleado: ")
            apellido = input("Apellido del empleado: ")
            cargo = input("Cargo del empleado (recepcionista, limpieza, etc.): ")
            sueldo = float(input("Sueldo del empleado: "))
            gestorBaseDatos.conectar()
            gestorBaseDatos.insertar_empleado(id_empleado, nombre, apellido, cargo, sueldo)
            gestorBaseDatos.desconectar()

        elif opcion == "6":
            gestorBaseDatos = GestorDB()
            gestorBaseDatos.borrar_base_de_datos()
            #esperar 1 segundo
            sleep(1)
            gestorBaseDatos.conectar()
            sleep(1)
            gestorBaseDatos.crear_tablas()
            sleep(1)
            gestorBaseDatos._insertar_datos_iniciales()
            sleep(1)
            
            #gestorBaseDatos.crear_tablas()
            print("Base de datos creada y tablas inicializadas con datos de ejemplo.")
            print("Mostrando datos de las tablas...")

        #opcion 7 
        # Mostrar Tablas
        elif opcion == "7":
            print("\nHabitaciones:")
            habitaciones = gestorBaseDatos.obtener_habitaciones()
            for habitacion in habitaciones:
                print(habitacion)

            print("\nClientes:")
            clientes = gestorBaseDatos.obtener_clientes()
            for cliente in clientes:
                print(cliente)

            print("\nReservas:")
            reservas = gestorBaseDatos.obtener_reservas()
            for reserva in reservas:
                print(reserva)

            print("\nFacturas:")
            facturas = gestorBaseDatos.obtener_facturas()
            for factura in facturas:
                print(factura)

            print("\nEmpleados:")
            empleados = gestorBaseDatos.obtener_empleados()
            for empleado in empleados:
                print(empleado)
            
        #opcion 8
        # Eliminar una habitacion
        elif opcion == "8":
            numero = int(input("Número de habitación a eliminar: "))
            gestorBaseDatos.conectar()
            gestorBaseDatos.eliminar_habitacion(numero)
            gestorBaseDatos.desconectar()


        elif opcion == "15":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
