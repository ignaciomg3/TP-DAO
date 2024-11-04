import sqlite3

class GestorDB:
    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name
        self.conn = None
        self.conectar()
        self.crear_tablas()

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
        consultas = [
            '''CREATE TABLE IF NOT EXISTS Habitacion (
                    numero INTEGER PRIMARY KEY,
                    tipo TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    precio_por_noche REAL NOT NULL
               )''',
            '''CREATE TABLE IF NOT EXISTS Cliente (
                    id_cliente INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    direccion TEXT,
                    telefono TEXT,
                    email TEXT
               )''',
            '''CREATE TABLE IF NOT EXISTS Reserva (
                    id_reserva INTEGER PRIMARY KEY,
                    id_cliente INTEGER,
                    numero_habitacion INTEGER,
                    fecha_entrada TEXT NOT NULL,
                    fecha_salida TEXT NOT NULL,
                    cantidad_personas INTEGER,
                    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                    FOREIGN KEY (numero_habitacion) REFERENCES Habitacion(numero)
               )''',
            '''CREATE TABLE IF NOT EXISTS Factura (
                    id_factura INTEGER PRIMARY KEY,
                    id_cliente INTEGER,
                    id_reserva INTEGER,
                    fecha_emision TEXT NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                    FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva)
               )''',
            '''CREATE TABLE IF NOT EXISTS Empleado (
                    id_empleado INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    cargo TEXT NOT NULL,
                    sueldo REAL NOT NULL
               )'''
        ]

        try:
            for consulta in consultas:
                self.ejecutar_consulta(consulta)
            print("Tablas creadas/verificadas correctamente.")
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")

    def insertar_habitacion(self, numero, tipo, estado, precio_por_noche):
        """Inserta una nueva habitación en la base de datos."""
        consulta = '''
            INSERT INTO Habitacion (numero, tipo, estado, precio_por_noche)
            VALUES (?, ?, ?, ?)
        '''
        resultado = self.ejecutar_consulta(consulta, (numero, tipo, estado, precio_por_noche))
        if resultado:
            print("Habitación insertada correctamente.")

    def obtener_habitaciones(self):
        """Obtiene todas las habitaciones de la base de datos."""
        consulta = 'SELECT * FROM Habitacion'
        cursor = self.ejecutar_consulta(consulta)

        if cursor:
            habitaciones = cursor.fetchall()
            print("Habitaciones obtenidas correctamente.")
            return habitaciones
        else:
            print("No se pudieron obtener las habitaciones.")
            return []

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
        resultado = self.ejecutar_consulta(consulta, (id_empleado, nombre, apellido, cargo, sueldo))
        if resultado:
            print("Empleado insertado correctamente.")
