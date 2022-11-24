from empleado import Gerente
from empleado import Tecnico
from empleado import Gestora
from empleado import Administrador
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from reportes import ReporteProgramacion
from programacion import Matutino
from programacion import Vespertino

empleados=[
    Gerente("Roberto","uno","$20,000.00",Matutino()),
    Gestora("Alejandra","dos","$8,000.00",Matutino()),
    Gestora("Selene","tres","$8,000.00",Matutino()),
    Tecnico("Artemio","cuatro","$9,000.00",Vespertino()),
    Tecnico("Salvador","cinco","$9,000.00",Vespertino()),
    Tecnico("Ronaldo","seis","$9,000.00",Matutino()),
    Administrador("Marco","siete","$15,000.00",Matutino()),   
]
reportes=[
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]

for r in reportes:
    r.print_reporte()

##reporteContabilidad = ReporteContabilidad(empleados)
##reporteContabilidad.reporte_contabilidad()
##ReporteEmpleados = ReporteEmpleados(empleados)
##ReporteEmpleados.reporte_empleados()