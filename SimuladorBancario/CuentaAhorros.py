__author__ = "Benjamin Andres Urbano Zuñiga"
__license__ = "GPL"
__version__ =  "1.0.0"
__email__= "benjamin.urbano@campusucc.edu.co"



__method__="ConsignarValor"
__parameter__="nuevoValor"
__returns__="saldo"
__Description__="metodo que actualiza el saldo en cuenta"
saldoCuentaAhorros = 0
interesMensual=0

class CuentaAhoros:
    def ConsignarValor(self,nuevoValor):
        return self.saldo

    __method__="MostrarSaldo"
    __parameter__=""
    __returns__="Saldo de la cuenta"
    __Description__="metodo que retorna el saldo de la cuenta cliente"
    def DarSaldoAhorros(self):
        return self.saldo
    
    __method__="Retiro"
    __parameter__="monto"
    __returns__="valorRetiro"
    __Description__="metodo que indica el valor del retiro de la cuenta"
    def RetirarValor(self,monto):
        self.saldo = monto
    
    __method__="MostrarInteres"
    __parameter__=""
    __returns__="Interes"
    __Description__="metodo que indica el interes de cada cuenta"
    def DarIntereMensual(self):
        return self.interesMensual

    __method__="CambiarSaldo"
    __parameter__=""
    __returns__="SaldoMes"
    __Description__="metodo que actualiza el saldo mensual"
    def ActualizarSaldoPorPasoMes(self):
        return self.saldo