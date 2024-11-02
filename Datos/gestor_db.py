import sqlite3

class GestorDB:
    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name
        self.conn = None

    def conectar(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print("Conexión a la base de datos establecida.")
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
            cursor = self.conn.cursor()
            cursor.execute(consulta, parametros)
            self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
    
    def crear_tablas(self):
        """Crea las tablas necesarias en la base de datos."""
        try:
            self.conectar()
            cursor = self.conn.cursor()
            
            # Crear tabla Habitacion
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Habitacion (
                    numero INTEGER PRIMARY KEY,
                    tipo TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    precio_por_noche REAL NOT NULL
                )
            ''')

            # Crear tabla Cliente
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Cliente (
                    id_cliente INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    direccion TEXT,
                    telefono TEXT,
                    email TEXT
                )
            ''')

            # Crear tabla Reserva
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Reserva (
                    id_reserva INTEGER PRIMARY KEY,
                    id_cliente INTEGER,
                    numero_habitacion INTEGER,
                    fecha_entrada TEXT NOT NULL,
                    fecha_salida TEXT NOT NULL,
                    cantidad_personas INTEGER,
                    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                    FOREIGN KEY (numero_habitacion) REFERENCES Habitacion(numero)
                )
            ''')

            # Crear tabla Factura
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Factura (
                    id_factura INTEGER PRIMARY KEY,
                    id_cliente INTEGER,
                    id_reserva INTEGER,
                    fecha_emision TEXT NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                    FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva)
                )
            ''')

            # Crear tabla Empleado
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Empleado (
                    id_empleado INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    cargo TEXT NOT NULL,
                    sueldo REAL NOT NULL
                )
            ''')

            self.conn.commit()
            print("Tablas creadas exitosamente.")
        
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")
        
        finally:
            self.desconectar()

    def insertar_habitacion(self, numero, tipo, estado, precio_por_noche):
        """Inserta una nueva habitación en la base de datos."""
        consulta = '''
            INSERT INTO Habitacion (numero, tipo, estado, precio_por_noche)
            VALUES (?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (numero, tipo, estado, precio_por_noche))
        print("Habitación insertada correctamente.")

    def insertar_cliente(self, id_cliente, nombre, apellido, direccion, telefono, email):
        """Inserta un nuevo cliente en la base de datos."""
        consulta = '''
            INSERT INTO Cliente (id_cliente, nombre, apellido, direccion, telefono, email)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (id_cliente, nombre, apellido, direccion, telefono, email))
        print("Cliente insertado correctamente.")

    def insertar_reserva(self, id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas):
        """Inserta una nueva reserva en la base de datos."""
        consulta = '''
            INSERT INTO Reserva (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, cantidad_personas))
        print("Reserva insertada correctamente.")

    def insertar_factura(self, id_factura, id_cliente, id_reserva, fecha_emision, total):
        """Inserta una nueva factura en la base de datos."""
        consulta = '''
            INSERT INTO Factura (id_factura, id_cliente, id_reserva, fecha_emision, total)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (id_factura, id_cliente, id_reserva, fecha_emision, total))
        print("Factura insertada correctamente.")

    def insertar_empleado(self, id_empleado, nombre, apellido, cargo, sueldo):
        """Inserta un nuevo empleado en la base de datos."""
        consulta = '''
            INSERT INTO Empleado (id_empleado, nombre, apellido, cargo, sueldo)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.ejecutar_consulta(consulta, (id_empleado, nombre, apellido, cargo, sueldo))
        print("Empleado insertado correctamente.")

        