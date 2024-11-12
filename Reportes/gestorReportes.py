from Reportes.reporte_reserva import listar_reservas
from Reportes.reporte_ingresos import generar_reporte_ingresos
from Reportes.reporte_ocupacion import reporte_ocupacion_promedio
from Reportes.validaciones import *
from Reportes.graficos import graficar_ocupacion_promedio, graficar_ingresos_mensuales
from Datos.gestor_db import GestorDB

class GestorReportes:
    def __init__(self, gestor_db=None):
        self.reportes = []
        self.gestor_db = gestor_db or GestorDB()

    def generar_reporte_reservas(self, fecha_inicio, fecha_fin):
        """Genera un reporte de todas las reservas en un periodo de tiempo."""
        self.gestor_db.conectar()
        reservas = listar_reservas(fecha_inicio, fecha_fin)
        self.gestor_db.desconectar()
        self.reportes.append(reservas)
        return reservas

    def generar_reporte_ingresos(self, mes):
        """Genera un reporte de ingresos para un mes específico."""
        self.gestor_db.conectar()
        mes_formateado = f"{mes[:7]}-01"
        reporte = generar_reporte_ingresos(mes_formateado)
        self.gestor_db.desconectar()
        return reporte

    def generar_reporte_ocupacion(self, mes):
        """Genera un reporte de ocupación promedio por tipo de habitación para un mes específico."""
        self.gestor_db.conectar()
        mes_formateado = f"{mes[:7]}-01"
        ocupacion = reporte_ocupacion_promedio(mes_formateado)
        self.gestor_db.desconectar()
        self.reportes.append(ocupacion)
        return ocupacion

    def graficar_ocupacion_promedio(self, mes):
        """Genera un gráfico de barras mostrando la ocupación promedio por tipo de habitación para un mes específico."""
        self.gestor_db.conectar()
        mes_formateado = f"{mes[:7]}-01"
        graficar_ocupacion_promedio(mes_formateado)
        self.gestor_db.desconectar()

    def graficar_ingresos_mensuales(self, mes):
        """Genera un gráfico de líneas mostrando los ingresos mensuales para un mes específico."""
        self.gestor_db.conectar()
        mes_formateado = f"{mes[:7]}-01"
        graficar_ingresos_mensuales(mes_formateado)
        self.gestor_db.desconectar()

    def listar_reportes(self):
        """Lista todos los reportes generados."""
        return self.reportes

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        self.gestor_db.desconectar()