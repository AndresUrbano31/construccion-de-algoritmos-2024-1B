__author__ = "Benjamin Andres Urbano Zuñiga"
__license__ = "GPL"
__version__ =  "1.0.0"
__email__= "benjamin.urbano@campusucc.edu.co"



__method__="ConsignarValor"
__parameter__="nuevoValor"
__returns__="saldo"
__Description__="metodo que actualiza el saldo en cuenta"




class CuentaCorriente:
    
    """#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#"""
    __saldoCuentaCorriente = 0
    
    __method__="MostrarSaldo"
    __parameter__=""
    __returns__="Saldo de la cuenta"
    __Description__="metodo que retorna el saldo de la cuenta "
    def DarSaldoCorriente(self):
     return self.__saldoCuentaCorriente
    
    __method__="ConsignarSaldo"
    __parameter__="Metodo"
    __returns__=""
    __Description__="metodo que Permite consignar un monto a la cuenta "
    
    def ConsignarSaldo (self,monto):
        self.__saldoCuentaCorriente = self.__saldoCuentaCorriente+monto
    
    

    
    
    __method__="RetirarSaldo"
    __parameter__="Monto"
    __returns__="valorRetiro"
    __Description__="Metodo que permite retirar saldo"
    def RetirarSaldo(self,monto):
     self.__saldoCuentaCorriente = self.__saldoCuentaCorriente-monto

    __method__="CambiarSaldo"
    __parameter__=""
    __returns__="SaldoMes"
    __Description__="metodo que actualiza el saldo mensual"
    def ActualizarSaldoPorPasoMes(self):
        return self.__saldoCuentaCorriente