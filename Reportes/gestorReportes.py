from Reportes.reporte_reserva import listar_reservas
from Reportes.reporte_ingresos import generar_reporte_ingresos
from Reportes.reporte_ocupacion import reporte_ocupacion_promedio
from Reportes.validaciones import *
from Reportes.graficos import graficar_ocupacion_promedio, graficar_ingresos_mensuales

class GestorReportes:
    def __init__(self):
        self.reportes = []

    def generar_reporte_reservas(self, fecha_inicio, fecha_fin):
        """Genera un reporte de todas las reservas en un periodo de tiempo."""
        reservas = listar_reservas(fecha_inicio, fecha_fin)
        self.reportes.append(reservas)
        return reservas

    def generar_reporte_ingresos(self):
        return generar_reporte_ingresos()

    def generar_reporte_ocupacion(self):
        """Genera un reporte de ocupación promedio por tipo de habitación."""
        ocupacion = reporte_ocupacion_promedio()
        self.reportes.append(ocupacion)
        return ocupacion

    def verificar_reserva(self, numero_habitacion, fecha_entrada, fecha_salida):
        """Verifica si hay superposición de reservas para la misma habitación."""
        return verificar_superposicion_reserva(numero_habitacion, fecha_entrada, fecha_salida)
    
    def verificar_asignaciones(self, id_empleado, fecha):
        """Verifica que los empleados asignados a habitaciones no tengan más de 5 asignaciones diarias.."""
        return validar_empleado_asignaciones(id_empleado, fecha)

    def graficar_ocupacion_promedio(self):
        """Genera un gráfico de barras mostrando la ocupación promedio por tipo de habitación."""
        graficar_ocupacion_promedio()

    def graficar_ingresos_mensuales(self):
        """Genera un gráfico de líneas mostrando los ingresos mensuales."""
        graficar_ingresos_mensuales()

    def listar_reportes(self):
        """Lista todos los reportes generados."""
        return self.reportes