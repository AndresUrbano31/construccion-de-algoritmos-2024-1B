__author__ = "Benjamin Andres Urbano Zuñiga"
__license__ = "GPL"
__version__ =  "1.0.0"
__email__= "benjamin.urbano@campusucc.edu.co"

from Empleado.Fecha import Fecha
class Empleado: 
    #Aqui inicia la declaracion de la  clase
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    
    nombre =""
    apellido = ""
    salario=0
    
    """#----------------------------------------------------------------
    # 1 =Masculino, 2= Femenino
    ----------------------------------------------------------------#"""
    sexo = False

    """#----------------------------------------------------------------
    # Asociacion = traer una class que esta en otro archivo 
    ----------------------------------------------------------------#"""
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    """#----------------------------------------------------------------
    # Metdos 
    ----------------------------------------------------------------#"""
    __method__="CambiarSalario"
    __parameter__="nuevoSalario"
    __returns__="Salario"
    __Description__="metodo que actualiza el salario del empleado"
    
    #este metodo retorna el nombre del empleado
    def DarNombre(self):
        #Aqui va mi codigo
        return self.nombre
     
    def CambiarSalario(self, nuevoSalario):
        #Aqui va mi codigo
        self.salario = nuevoSalario
    
    def DarSalario(self):
        #Aqui va mi codigo
        return self.salario
    
    def CunsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha
    
    __method__="CalcularSalarioAnual"
    __parameter__="Ninguno"
    __returns__="Salario Anual"
    __Description__="Muestra el salario anual del empleado"
    
    def CalcularSalarioAnual(self):
        #Aqui va mi codigo
        # total = self.salario*12
        # return total
        return self.salario*12
    
    __method__="CalcularImpuestoSalarioAnual"
    __parameter__="Ninguno"
    __returns__="Impuesto Salario Anual"
    __Description__="Muestra el Impuesto del salario anual del empleado"
    
    def CalcularImpuestoSalarioAnual(self):
        #Aqui inicia mi codigo 
        #Forma 1
        # salarioAnual = self.CalcularImpuestoSalarioAnual()
        # impuestoAnual = salarioAnual*0.19
        # return impuestoAnual
        #Forma 2 
        return self.CalcularSalarioAnual()*0.19
    
    __method__="CalcularImpuestoSalarioMensual"
    __parameter__="Ninguno"
    __returns__="Impuesto Salario Mensual"
    __Description__="Muestra el Impuesto del salario Mensual del empleado"
    
    def CalcularImpuestoSalarioMensual(self):
        return self.DarSalario()*0.19