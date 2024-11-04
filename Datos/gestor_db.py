import sqlite3
import os

DB_PATH = "Datos/BaseDatos.db"
class GestorDB:
    def __init__(self, db_name=DB_PATH):
        self.db_name = db_name
        self.conn = None
        print("Constructor de GestorBD.")

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
        
        # Llamar a otras funciones de creación de tablas aquí...
        
        self._insertar_datos_iniciales()
        #self.desconectar()
        print("Tablas creadas y datos iniciales insertados..función _crear_tablas().")

    def _crear_tabla_habitaciones(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS habitaciones (
                                numero INTEGER PRIMARY KEY,
                                tipo TEXT,
                                estado TEXT,
                                precio_por_noche REAL)''')
        print("Tabla habitaciones creada correctamente.")
        
    def _crear_tabla_clientes(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT,
                                apellido TEXT,
                                direccion TEXT,
                                telefono TEXT,
                                email TEXT)''')
        print("Tabla clientes creada correctamente.")
        
    def _crear_tabla_empleados(self):
        """Crea la tabla empleados si no existe."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                               id INTEGER PRIMARY KEY,
                               nombre TEXT NOT NULL,
                               apellido TEXT NOT NULL,
                               cargo TEXT NOT NULL,
                               sueldo REAL NOT NULL
                            )''')
        self.conn.commit()

    def _crear_tabla_reservas(self):
        """Crea la tabla reservas si no existe."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                               id INTEGER PRIMARY KEY,
                               id_cliente INTEGER NOT NULL,
                               numero_habitacion INTEGER NOT NULL,
                               fecha_entrada TEXT NOT NULL,
                               fecha_salida TEXT NOT NULL,
                               cantidad_personas INTEGER NOT NULL
                            )''')
        self.conn.commit()
    
    def _crear_tabla_facturas(self):
        """Crea la tabla facturas si no existe."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS facturas (
                               id INTEGER PRIMARY KEY,
                               id_cliente INTEGER NOT NULL,
                               id_reserva INTEGER NOT NULL,
                               fecha_emision TEXT NOT NULL,
                               total REAL NOT NULL
                            )''')
        self.conn.commit()

#***************************** INSERTAR ***********************
    
    def _insertar_datos_iniciales(self):
        # Verificar si la tabla tiene datos
        self.cursor.execute('SELECT COUNT(*) FROM habitaciones')
        if self.cursor.fetchone()[0] == 0:
            # Insertar datos de prueba en la tabla habitaciones
            self.cursor.executemany('''INSERT INTO habitaciones (numero, tipo, estado, precio_por_noche)
                                       VALUES (?, ?, ?, ?)''', [
                                           (101, 'simple', 'disponible', 50.0),
                                           (102, 'doble', 'ocupada', 75.0),
                                           (201, 'suite', 'disponible', 150.0)
                                       ])
            self.conn.commit()
            # Insertar datos de prueba en la tabla clientes
            self.cursor.executemany('''INSERT INTO clientes (id, nombre, apellido, direccion, telefono, email)
                                       VALUES (?, ?, ?, ?, ?, ?)''', [
                                           (1, 'Juan', 'Pérez', 'Calle 123', '123456789', 'juan.perez@mail.com'),
                                           (2, 'Ana', 'Gómez', 'Avenida 456', '987654321', 'ana.gomez@mail.com')
                                       ])
            self.conn.commit()

            self.cursor.executemany('''INSERT INTO empleados (id, nombre, apellido, cargo, sueldo)
                           VALUES (?, ?, ?, ?, ?)''', [
                               (1, 'Pedro', 'Lopez', 'Recepcionista', 2500.00),
                               (2, 'Laura', 'Martinez', 'Servicio de limpieza', 1800.00),
                               (3, 'Carlos', 'Gomez', 'Conserje', 2200.00)
                           ])
            self.conn.commit()

            self.cursor.executemany('''INSERT INTO reservas (id, cliente_id, habitacion_id, fecha_entrada, fecha_salida, cantidad_personas)
                           VALUES (?, ?, ?, ?, ?, ?)''', [
                               (1, 1, 101, '2024-03-01', '2024-03-05', 2),
                               (2, 2, 102, '2024-03-10', '2024-03-15', 1)
                           ])
            self.conn.commit()

            
            self.cursor.executemany('''INSERT INTO facturas (id, cliente_id, reserva_id, fecha_emision, total)
                           VALUES (?, ?, ?, ?, ?)''', [
                               (1, 1, 1, '2024-03-05', 500.00),
                               (2, 2, 2, '2024-03-15', 300.00)
                           ])
            self.conn.commit()

    def insertar_habitacion(self, numero, tipo, estado, precio_por_noche):
        """Inserta una nueva habitación en la base de datos."""
        consulta = '''
            INSERT INTO Habitacion (numero, tipo, estado, precio_por_noche)
            VALUES (?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (numero, tipo, estado, precio_por_noche))
        if resultado:
            print("Habitación insertada correctamente.")
    
    def insertar_cliente(self, id_cliente, nombre, apellido, direccion, telefono, email):
        """Inserta un nuevo cliente en la base de datos."""
        consulta = '''
            INSERT INTO Cliente (id_cliente, nombre, apellido, direccion, telefono, email)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (id_cliente, nombre, apellido, direccion, telefono, email))
        if resultado:
            print("Cliente insertado correctamente.")
    
    def insertar_reserva(self, id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas):
        """Inserta una nueva reserva en la base de datos."""
        consulta = '''
            INSERT INTO Reserva (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas))
        if resultado:
            print("Reserva insertada correctamente.")

    def insertar_factura(self, id_factura, id_cliente, id_reserva, fecha_emision, total):
        """Inserta una nueva factura en la base de datos."""
        consulta = '''
            INSERT INTO Factura (id_factura, id_cliente, id_reserva, fecha_emision, total)
            VALUES (?, ?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (id_factura, id_cliente, id_reserva, fecha_emision, total))
        if resultado:
            print("Factura insertada correctamente.")

    def insertar_empleado(self, id_empleado, nombre, apellido, cargo, sueldo):
        """Inserta un nuevo empleado en la base de datos."""
        consulta = '''
            INSERT INTO Empleado (id_empleado, nombre, apellido, cargo, sueldo)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (id_empleado, nombre, apellido, cargo, sueldo))
        print("Empleado insertado correctamente.")
    
    #***************************** CONSULTAS ***********************
    def obtener_habitaciones(self):
        """Obtiene todas las habitaciones de la base de datos."""
        consulta = 'SELECT * FROM habitaciones'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            habitaciones = cursor.fetchall()
            return habitaciones
        else:
            return []
   
    def obtener_habitaciones(self):
        #mostrar habitaciones
        consulta = 'SELECT * FROM Habitacion'
        cursor = self.ejecutar_consulta(consulta)

        if cursor:
            habitaciones = cursor.fetchall()
            print("Habitaciones obtenidas correctamente.")
            return habitaciones
        else:
            print("No se pudieron obtener las habitaciones.")
            return []

    def obtener_clientes(self):
        """Obtiene todos los clientes de la base de datos."""
        consulta = 'SELECT * FROM clientes'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            clientes = cursor.fetchall()
            return clientes
        else:
            return []
        
    def obtener_clientes2(self):
        #mostrar clientes
        consulta = 'SELECT * FROM Cliente'
        cursor = self.ejecutar_consulta(consulta)

        if cursor:
            clientes = cursor.fetchall()
            print("Clientes obtenidas correctamente.")
            return clientes
        else:
            print("No se pudieron obtener los clientes.")
            return []
    
    def obtener_reservas(self):
        """Obtiene todas las reservas de la base de datos."""
        consulta = 'SELECT * FROM Reserva'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            reservas = cursor.fetchall()
            return reservas
        else:
            return []
        
    def obtener_facturas(self):
        """Obtiene todas las facturas de la base de datos."""
        consulta = 'SELECT * FROM Factura'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            facturas = cursor.fetchall()
            return facturas
        else:
            return []
        
    def obtener_empleados(self):
        """Obtiene todos los empleados de la base de datos."""
        consulta = 'SELECT * FROM Empleado'
        cursor = self.ejecutar_consulta(consulta)
        if cursor:
            empleados = cursor.fetchall()
            return empleados
        else:
            return []

    #*********************** REPORTES **************************



