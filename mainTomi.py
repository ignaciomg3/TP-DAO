from Datos.gestor_db import GestorDB
from Reportes.gestorReportes import GestorReportes

def main():
    gestor = GestorDB()
    gestor_reportes= GestorReportes()
    
    while True:
        print("\n********** Menú del Sistema de Gestión de Hotel **********")
        print("1. Registrar una nueva habitación")
        print("2. Registrar un nuevo cliente")
        print("3. Realizar una reserva")
        print("4. Generar una factura")
        print("5. Registrar un empleado")
        print("6. Menú de Reportes")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Ejemplo de registro de una habitación
            numero = int(input("Número de habitación: "))
            tipo = input("Tipo de habitación (simple, doble, suite): ")
            estado = input("Estado de la habitación (disponible/ocupada): ")
            precio_por_noche = float(input("Precio por noche: "))
            gestor.conectar()
            gestor.insertar_habitacion(numero, tipo, estado, precio_por_noche)
            gestor.desconectar()

        elif opcion == "2":
            # Ejemplo de registro de un cliente
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            direccion = input("Dirección del cliente: ")
            telefono = input("Teléfono del cliente: ")
            email = input("Email del cliente: ")
            gestor.conectar()
            gestor.insertar_cliente(id_cliente, nombre, apellido, direccion, telefono, email)
            gestor.desconectar()

        elif opcion == "3":
            # Ejemplo de realizar una reserva
            id_reserva = int(input("ID de la reserva: "))
            id_cliente = int(input("ID del cliente: "))
            numero_habitacion = int(input("Número de la habitación: "))
            fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
            fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")
            cantidad_personas = int(input("Cantidad de personas: "))
            gestor.conectar()
            gestor.insertar_reserva(id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas)
            gestor.desconectar()

        elif opcion == "4":
            # Ejemplo de generación de una factura
            id_factura = int(input("ID de la factura: "))
            id_cliente = int(input("ID del cliente: "))
            id_reserva = int(input("ID de la reserva: "))
            fecha_emision = input("Fecha de emisión (YYYY-MM-DD): ")
            total = float(input("Total a pagar: "))
            gestor.conectar()
            gestor.insertar_factura(id_factura, id_cliente, id_reserva, fecha_emision, total)
            gestor.desconectar()

        elif opcion == "5":
            # Ejemplo de registro de un empleado
            id_empleado = int(input("ID del empleado: "))
            nombre = input("Nombre del empleado: ")
            apellido = input("Apellido del empleado: ")
            cargo = input("Cargo del empleado (recepcionista, limpieza, etc.): ")
            sueldo = float(input("Sueldo del empleado: "))
            gestor.conectar()
            gestor.insertar_empleado(id_empleado, nombre, apellido, cargo, sueldo)
            gestor.desconectar()

        elif opcion == "6":
            print("\n********** Menú de Reportes **********")
            print("1. Listar todas las reservas en un periodo")
            print("2. Generar reporte de ingresos por habitaciones y servicios extras")
            print("3. Reporte de ocupación promedio por tipo de habitación")
            print("4. Gráfico de ocupación promedio")
            print("5. Gráfico de ingresos mensuales")
            print("6. Regresar al menú principal")

            opcion_reporte = input("Seleccione una opción: ")

            if opcion_reporte == "1":
                # Aquí se solicitarán las fechas y se llamará al método correspondiente
                numero_habitacion= input("Ingrese el número de su habitación: ")
                fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
                reportes = gestor_reportes.generar_reporte_reservas (fecha_inicio, fecha_fin)
                print(reportes)
                

            elif opcion_reporte == "2":
                # Aquí se generará el reporte de ingresos
                ingresos_habitaciones = gestor_reportes.generar_reporte_ingresos()

                print("\nReporte de Ingresos por Habitación:")
                for numero_habitacion, total_ingresos in ingresos_habitaciones.items():
                    print(f"Habitación {numero_habitacion}: ${total_ingresos:.2f}")

            elif opcion_reporte == "3":
                # Aquí se generará el reporte de ocupación
                ocupacion_report = gestor_reportes.generar_reporte_ocupacion()
                print(ocupacion_report)

            elif opcion_reporte == "4":
                gestor_reportes.graficar_ocupacion_promedio()
                
            elif opcion_reporte == "5":
                gestor_reportes.graficar_ingresos_mensuales()
                
            elif opcion_reporte == "6":
                continue

            else:
                print("Opción no válida. Por favor, intente de nuevo.")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
