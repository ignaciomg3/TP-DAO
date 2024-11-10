import sqlite3
import os

DB_PATH = "Datos/BaseDatos.db"

class GestorDB:
    _instance = None  # Variable de clase para almacenar la única instancia de GestorDB

    def __new__(cls, db_name=DB_PATH):
        # Verifica si _instance es None, lo que significa que aún no se ha creado una instancia
        if cls._instance is None:
            # Si no hay una instancia, se crea una usando __new__ del padre (super)
            cls._instance = super(GestorDB, cls).__new__(cls)
            # Asigna el nombre de la base de datos a la instancia única
            cls._instance.db_name = db_name
            # Inicializa la variable de conexión como None para más adelante establecer la conexión a la BD
            cls._instance.conn = None
            print("Creando la única instancia de GestorDB (Singleton).")
        # Devuelve la instancia única
        return cls._instance
    
    def __init__(self, db_name=DB_PATH):
        # Este método está intencionalmente vacío. La inicialización en el Singleton se maneja en __new__.
        # De esta forma, __init__ no sobreescribe la instancia existente.
        pass
        
        # self.db_name = db_name
        # self.conn = None
        # print("Constructor de GestorBD.")


    def borrar_base_de_datos(self):
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
            print("Base de datos borrada exitosamente.")
        else:
            print("No se encontró ninguna base de datos para borrar.")

    def conectar(self):
        """Establece la conexión con la base de datos."""
        try:
            if self.conn is None:
                self.conn = sqlite3.connect(self.db_name)
                self.cursor = self.conn.cursor()  # Asegúrate de que esta línea esté presente
            print("Conexión a la base de datos establecida..")
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")

    def desconectar(self):
        """Cierra la conexión con la base de datos."""
        if self.conn:
            self.conn.close()
            print("Conexión a la base de datos cerrada.")

    def mostrar_tablas(self):
        """Muestra las tablas de la base de datos."""
        self.conectar()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = self.cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])
        ##self.desconectar()()

    def ejecutar_consulta(self, consulta, parametros=()):
        """Ejecuta una consulta SQL con parámetros opcionales."""
        try:
            if self.conn is None:
                self.conectar()  # Asegúrate de que la conexión esté abierta
            cursor = self.conn.cursor()
            cursor.execute(consulta, parametros)
            self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

#***************************** CREAR TABLAS ***********************
    def crear_tablas(self):
        self.conectar()
        self._crear_tabla_habitaciones()
        self._crear_tabla_clientes()
        self._crear_tabla_empleados()
        self._crear_tabla_reservas()
        self._crear_tabla_facturas()
        # Llamar a otras funciones de creación de tablas aquí...
        
        self._insertar_datos_iniciales()
        ##self.desconectar()()
        print("Tablas creadas y datos iniciales insertados..función _crear_tablas().")

    def _crear_tabla_habitaciones(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS habitaciones (
                                numero INTEGER,
                                tipo TEXT,
                                estado TEXT,
                                precio_por_noche REAL)''')
        print("Tabla habitaciones creada correctamente.")
        
    def _crear_tabla_clientes(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                                id_cliente INTEGER,
                                nombre TEXT,
                                apellido TEXT,
                                direccion TEXT,
                                telefono TEXT,
                                email TEXT)''')
        print("Tabla clientes creada correctamente.")
        
    def _crear_tabla_empleados(self):
        """Crea la tabla empleados si no existe."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                               id_empleado INTEGER,
                               nombre TEXT NOT NULL,
                               apellido TEXT NOT NULL,
                               cargo TEXT NOT NULL,
                               sueldo REAL NOT NULL
                            )''')
        #self.conn.commit()
        print("Tabla empleados creada correctamente.")

    def _crear_tabla_reservas(self):
        """Crea la tabla reservas si no existe."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                               id_reserva INTEGER,
                               id_cliente INTEGER NOT NULL,
                               numero_habitacion INTEGER NOT NULL,
                               fecha_entrada TEXT NOT NULL,
                               fecha_salida TEXT NOT NULL,
                               cantidad_personas INTEGER NOT NULL
                            )''')
        print("Tabla reservas creada correctamente.")
        #self.conn.commit()
    
    def _crear_tabla_facturas(self):
        """Crea la tabla facturas si no existe."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS facturas (
                               id_factura INTEGER,
                               id_cliente INTEGER NOT NULL,
                               id_reserva INTEGER NOT NULL,
                               fecha_emision TEXT NOT NULL,
                               total REAL NOT NULL
                            )''')
        print("Tabla facturas creada correctamente.")
        self.conn.commit()

#***************************** INSERTAR DATOS RANDOMS***********************
    
    def _insertar_datos_iniciales(self):
        # Verificar si la tabla tiene datos
        
        # Insertar datos de prueba en la tabla habitaciones
        self.cursor.executemany('''INSERT INTO habitaciones (numero, tipo, estado, precio_por_noche)
                                    VALUES (?, ?, ?, ?)''', [
                                        (101, 'simple', 'disponible', 50.0),
                                        (102, 'doble', 'ocupada', 75.0),
                                        (103, 'suite', 'disponible', 150.0),
                                        (104, 'simple', 'ocupada', 50.0),
                                        (105, 'doble', 'disponible', 80.0),
                                        (201, 'suite', 'ocupada', 160.0),
                                        (202, 'simple', 'disponible', 55.0),
                                        (203, 'doble', 'disponible', 78.0),
                                        (204, 'suite', 'disponible', 155.0),
                                        (205, 'simple', 'ocupada', 52.0),
                                        (301, 'doble', 'ocupada', 77.0),
                                        (302, 'suite', 'disponible', 170.0)
                                    ])
        self.conn.commit()
        # Insertar datos de prueba en la tabla clientes
        self.cursor.executemany('''INSERT INTO clientes (id_cliente, nombre, apellido, direccion, telefono, email)
                                    VALUES (?, ?, ?, ?, ?, ?)''', [
                                        (1, 'Juan', 'Pérez', 'Calle 123', '123456789', 'juan.perez@mail.com'),
                                        (2, 'Ana', 'Gómez', 'Avenida 456', '987654321', 'ana.gomez@mail.com'),
                                        (3, 'Luis', 'Torres', 'Calle San Martín 789', '1122334455', 'luis.torres@mail.com'),
                                        (4, 'Carla', 'Fernandez', 'Avenida Libertad 101', '2233445566', 'carla.fernandez@mail.com'),
                                        (5, 'Miguel', 'Lopez', 'Calle Roca 321', '3344556677', 'miguel.lopez@mail.com'),
                                        (6, 'Sofia', 'Ramirez', 'Pasaje del Sol 202', '4455667788', 'sofia.ramirez@mail.com'),
                                        (7, 'Andres', 'Hernandez', 'Calle 9 de Julio 150', '5566778899', 'andres.hernandez@mail.com'),
                                        (8, 'Lucia', 'Martinez', 'Boulevard Mitre 45', '6677889900', 'lucia.martinez@mail.com'),
                                        (9, 'Pedro', 'Gonzalez', 'Calle 25 de Mayo 17', '7788990011', 'pedro.gonzalez@mail.com'),
                                        (10, 'Elena', 'Diaz', 'Avenida de los Pinos 88', '8899001122', 'elena.diaz@mail.com')
                                    ])
        self.conn.commit()

        self.cursor.executemany('''INSERT INTO empleados (id_empleado, nombre, apellido, cargo, sueldo)
                        VALUES (?, ?, ?, ?, ?)''', [
                            (1, 'Pedro', 'Lopez', 'Recepcionista', 2500.00),
                            (2, 'Laura', 'Martinez', 'Servicio de limpieza', 1800.00),
                            (3, 'Carlos', 'Gomez', 'Conserje', 2200.00),
                            (4, 'Marta', 'Fernandez', 'Gerente', 4000.00),
                            (5, 'Javier', 'Ramirez', 'Mantenimiento', 2100.00),
                            (6, 'Sofia', 'Diaz', 'Recepcionista', 2600.00),
                            (7, 'Andres', 'Torres', 'Servicio de limpieza', 1850.00),
                            (8, 'Isabel', 'Hernandez', 'Conserje', 2300.00),
                            (9, 'Luis', 'Morales', 'Cocinero', 2700.00),
                            (10, 'Paula', 'Castro', 'Servicio al cliente', 2400.00)
                        ])
        self.conn.commit()

        self.cursor.executemany('''INSERT INTO reservas (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas)
                        VALUES (?, ?, ?, ?, ?, ?)''', [
                            (1, 1, 101, '2024-03-01', '2024-03-05', 2),
                            (2, 2, 102, '2024-03-10', '2024-03-15', 1),
                            (3, 3, 103, '2024-03-05', '2024-03-08', 2),
                            (4, 4, 104, '2024-03-12', '2024-03-20', 3),
                            (5, 5, 201, '2024-03-18', '2024-03-22', 4),
                            (6, 6, 105, '2024-03-15', '2024-03-18', 1),
                            (7, 7, 106, '2024-03-09', '2024-03-13', 2),
                            (8, 8, 202, '2024-03-11', '2024-03-14', 3),
                            (9, 9, 107, '2024-03-07', '2024-03-10', 2),
                            (10, 10, 203, '2024-03-20', '2024-03-25', 1)
                        ])
        self.conn.commit()
        
        self.cursor.executemany('''INSERT INTO facturas (id_factura, id_cliente, id_reserva, fecha_emision, total)
                        VALUES (?, ?, ?, ?, ?)''', [
                            (1, 1, 1, '2024-03-05', 500.00),
                            (2, 2, 2, '2024-03-15', 300.00),
                            (3, 3, 3, '2024-03-08', 450.00),
                            (4, 4, 4, '2024-03-20', 700.00),
                            (5, 5, 5, '2024-03-22', 1200.00),
                            (6, 6, 6, '2024-03-18', 250.00),
                            (7, 7, 7, '2024-03-13', 400.00),
                            (8, 8, 8, '2024-03-14', 600.00),
                            (9, 9, 9, '2024-03-10', 350.00),
                            (10, 10, 10, '2024-03-25', 800.00),
                            (9, 9, 9, '2024-04-10', 350.00),
                            (10, 10, 10, '2024-04-25', 800.00)
                        ])
        self.conn.commit()

#***************************** INSERTAR DATOS ***********************

    def insertar_habitacion(self, numero, tipo, estado, precio_por_noche):
        """Inserta una nueva habitación en la base de datos."""
        consulta = '''
            INSERT INTO habitaciones (numero, tipo, estado, precio_por_noche)
            VALUES (?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (numero, tipo, estado, precio_por_noche))
        if resultado:
            print("Habitación insertada correctamente.")
    
    def insertar_cliente(self, id_cliente, nombre, apellido, direccion, telefono, email):
        """Inserta un nuevo cliente en la base de datos."""
        consulta = '''
            INSERT INTO clientes (id_cliente, nombre, apellido, direccion, telefono, email)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (id_cliente, nombre, apellido, direccion, telefono, email))
        if resultado:
            print("Cliente insertado correctamente.")
    
    def insertar_reserva(self, id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas):
        """Inserta una nueva reserva en la base de datos como una transacción."""
        consulta = '''
            INSERT INTO reservas (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        try:
            self.conectar()
            self.conn.execute('BEGIN TRANSACTION')
            resultado = self.ejecutar_consulta(consulta, (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas))
            if resultado:
                self.conn.commit()
                print("Reserva insertada correctamente.")
            else:
                self.conn.rollback()
                print("Error al insertar la reserva. Transacción revertida.")
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error al insertar la reserva: {e}. Transacción revertida.")
        finally:
            self.desconectar()

    def insertar_factura(self, id_factura, id_cliente, id_reserva, fecha_emision, total):
        """Inserta una nueva factura en la base de datos como una transacción."""
        consulta = '''
            INSERT INTO facturas (id_factura, id_cliente, id_reserva, fecha_emision, total)
            VALUES (?, ?, ?, ?, ?)
        '''
        try:
            self.conectar()
            self.conn.execute('BEGIN TRANSACTION')
            resultado = self.ejecutar_consulta(consulta, (id_factura, id_cliente, id_reserva, fecha_emision, total))
            if resultado:
                self.conn.commit()
                print("Factura insertada correctamente.")
            else:
                self.conn.rollback()
                print("Error al insertar la factura. Transacción revertida.")
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error al insertar la factura: {e}. Transacción revertida.")
        finally:
            self.desconectar()

    def insertar_empleado(self, id_empleado, nombre, apellido, cargo, sueldo):
        """Inserta un nuevo empleado en la base de datos."""
        consulta = '''
            INSERT INTO empleados (id_empleado, nombre, apellido, cargo, sueldo)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (id_empleado, nombre, apellido, cargo, sueldo))
        print("Empleado insertado correctamente.")
        
    
    #***************************** CONSULTAS ***********************
    def obtener_habitaciones(self):
        """Obtiene todas las habitaciones de la base de datos."""
        self.conectar()
        consulta = 'SELECT * FROM habitaciones'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            habitaciones = cursor.fetchall()
            #self.desconectar()
            return habitaciones
        else:
            print("No se pudieron obtener las habitaciones.")
            ##self.desconectar()
            return []
   
    def obtener_clientes(self):
        """Obtiene todos los clientes de la base de datos."""
        self.conectar()
        consulta = 'SELECT * FROM clientes'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            clientes = cursor.fetchall()
            #self.desconectar()
            print("Clientes obtenidos correctamente.")
            return clientes
        else:
            print("No se pudieron obtener los clientes.")
            #self.desconectar()
            return []
        
    
    def obtener_reservas(self):
        
        """Obtiene todas las reservas de la base de datos."""
        self.conectar()
        consulta = 'SELECT * FROM reservas'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            reservas = cursor.fetchall()
            #self.desconectar()
            return reservas
        else:
            #self.desconectar()
            return []
        
    def obtener_facturas(self):
        
        """Obtiene todas las facturas de la base de datos."""
        self.conectar()
        consulta = 'SELECT * FROM facturas'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            facturas = cursor.fetchall()
            self.desconectar()
            return facturas
        else:
            #self.desconectar()()
            return []
        
    def obtener_empleados(self):
        
        """Obtiene todos los empleados de la base de datos."""
        self.conectar()
        consulta = 'SELECT * FROM empleados'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            empleados = cursor.fetchall()
            #self.desconectar()()
            return empleados
        else:
            #self.desconectar()()
            return []

    #***************************** ACTUALIZAR DATOS ***********************

    #***************************** ELIMINAR DATOS ***********************

    def eliminar_habitacion(self, numero):
        """Elimina una habitación de la base de datos por su número."""
        consulta = 'DELETE FROM habitaciones WHERE numero = ?'
        resultado = self.ejecutar_consulta(consulta, (numero,))
        if resultado:
            print("Habitación eliminada correctamente.")

    def eliminar_cliente(self, id_cliente):
        """Elimina un cliente de la base de datos por su ID."""
        consulta = 'DELETE FROM clientes WHERE id_cliente = ?'
        resultado = self.ejecutar_consulta(consulta, (id_cliente,))
        if resultado:
            print("Cliente eliminado correctamente.")

    def eliminar_empleado(self, id_empleado):
        """Elimina un empleado de la base de datos por su ID."""
        consulta = 'DELETE FROM empleados WHERE id_empleado = ?'
        resultado = self.ejecutar_consulta(consulta, (id_empleado,))
        if resultado:
            print("Empleado eliminado correctamente.")

    def eliminar_reserva(self, id_reserva):
        """Elimina una reserva de la base de datos por su ID."""
        consulta = 'DELETE FROM reservas WHERE id_reserva = ?'
        resultado = self.ejecutar_consulta(consulta, (id_reserva,))
        if resultado:
            print("Reserva eliminada correctamente.")

    # def eliminar_factura(self, id_factura):
    #     """Elimina una factura de la base de datos por su ID."""
    #     consulta = 'DELETE FROM facturas WHERE id = ?'
    #     resultado = self.ejecutar_consulta(consulta, (id_factura,))
    #     if resultado:
    #         print("Factura eliminada correctamente.")

#***************************** INTERFAZ **************************
    
    def obtener_habitaciones_para_reserva(self):
        """Obtiene las habitaciones disponibles para reservar."""
        consulta ="""SELECT h.numero, h.tipo
        FROM habitaciones h
        where h.estado = 'disponible' """
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            habitaciones = cursor.fetchall()
            return habitaciones
        else:
            print("No se pudieron obtener las habitaciones.")
        return []
    

#*********************** REPORTES **************************



