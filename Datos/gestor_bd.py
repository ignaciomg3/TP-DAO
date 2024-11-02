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
