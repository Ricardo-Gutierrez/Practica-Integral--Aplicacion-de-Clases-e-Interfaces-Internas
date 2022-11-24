class Reporte:
    def __init__(self,lista_empleados):
        self._lista_empleados = lista_empleados

class ReporteContabilidad(Reporte):
    def print_reporte(self):
        print("::::::::::Reporte Contabilidad:::::::::::")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()},{e.salario}')


class ReporteEmpleados(Reporte):
    def print_reporte(self):
        print(":::::::::Reporte Empleados::::::::::::::")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()},{e.puesto}')

class ReporteProgramacion(Reporte):
    def print_reporte(self):
        print(":::::::::Reporte Programacion::::::::::::::")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()},{e.programacion.get_programacion_info()}')