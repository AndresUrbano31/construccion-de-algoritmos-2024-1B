__author__ = "Benjamin Andres Urbano Zuñiga"
__license__ = "GPL"
__version__ =  "1.0.0"
__email__= "benjamin.urbano@campusucc.edu.co"



"""#----------------------------------------------------------------
    # Fecha
----------------------------------------------------------------#"""
class Fecha:
    dia=0
    mes=0
    anio=0
   
    
    __returns__="Dia"
    __returns__="Mes"
    __returns__="Anio"

    __method__="DarDia"
    __parameter__="ninguno"
    __returns__="Dia"
    __Description__="metodo que regresa el dia"
    def DarDia(self):
        return self.dia
    __method__="DarMes"
    __parameter__="ninguno"
    __returns__="Mes"
    __Description__="metodo que regresa el Mes" 
    def DarMes(self):
         return self.mes
    
    __method__="DarAnio"
    __parameter__="ninguno"
    __returns__="Anio"
    __Description__="metodo que regresa el Anio"
    def DarAnio(self):
        return self.anio
    
    __method__="DarFecha"
    __parameter__="ninguno"
    __returns__="Anio"
    __Description__="metodo que regresa el Anio"
    def DarFecha(self):
        return self.dia+'/'+self.mes+'/'+self.anio # 12/5/2024
    
   