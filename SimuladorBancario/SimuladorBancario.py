__method__="ConsignarValor"
__parameter__="nuevoValor"
__returns__="saldo"
__Description__="metodo que actualiza el saldo en cuenta"

"""#----------------------------------------------------------------
    # Impoprtaciones 
    ----------------------------------------------------------------#"""

from CuentaAhorros import CuentaAhoros
from CuentaCorriente import CuentaCorriente
from CDT import Cdt

class SimuladorBancario:
    
    """#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#"""
    __cedula = ''
    __nombre = ''
    __mesActual= 0
    
    """#----------------------------------------------------------------
    # Asociacion = traer una class que esta en otro archivo 
    ----------------------------------------------------------------#"""
    __valorInvertido = Cdt()
    __cuentaAhorros = CuentaAhoros()
    __cuentaCorriente = CuentaCorriente()
    """#----------------------------------------------------------------
    # Metodos 
    ----------------------------------------------------------------#"""
    
    __method__="DepositarCuentaCorriente"
    __parameter__=""
    __returns__="Saldo de la cuenta"
    __Description__="metodo que permite depositar "
    def DepositarCuentaCorriente(self,monto):
        return self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__="CalcularSaldoTotal"
    __parameter__="Ninguno"
    __returns__="Saldo total de todas las cuentas"
    __Description__="Metodo que permite calcular el saldo total"
    
    def CalcularSaldoTotal(self):
        #METODO 1
        # total = self.__cuentaCorriente.DarSaldoCorriente()+self.__cuentaAhorros.DarSaldoAhorros()
        # return total
        #METODO 2
        return self.__cuentaCorriente.DarSaldoCorriente()+self.__cuentaAhorros.DarSaldoAhorros()
    
    __method__="PasarAhorroACorriente"
    __parameter__="Ninguno"
    __returns__="Ninguna"
    __Description__="Metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    
    def PasarAhorroACorriente(self):
        saldoAhorros = self.__cuentaAhorros.DarSaldoAhorros()
        self.__cuentaAhorros.RetirarValor(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)
        
    """#----------------------------------------------------------------
    # Taller
    ----------------------------------------------------------------#"""   
    
    __method__="Ahorrar"
    __parameter__="Monto"
    __returns__="Ninguna"
    __Description__="Metodo que permite pasar de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parametro"
    
    def Ahorrar(self, monto):
        saldoCorriente = self.__cuentaCorriente(monto)
        self.__cuentaCorriente.RetirarValor(saldoCorriente)
        self.__cuentaAhorros.ConsignarSaldo(saldoCorriente)
        
    __method__="retirarAhorro"
    __parameter__="Monto"
    __returns__="Ninguna"
    __Description__="Metodo que permite retirar un valor dado de la cuenta de ahorros"
    def retirarAhorro(self, monto):
        saldoAhorros = self.__cuentaAhorros(monto)
        self.__cuentaAhorros.RetirarValor(saldoAhorros)
        
    __method__="darSaldoCorriente"
    __parameter__="Ninguno"
    __returns__="Saldo en cuenta corriente"
    __Description__="Metodo que retorna el saldo que hay en la cuenta corriente"
    
    def darSaldoCorriente(self):
        return self.__cuentaCorriente.DarSaldoCorriente
    
    __method__="retirarTodo"
    __parameter__="Ninguno"
    __returns__="Ninguna"
    __Description__="Metodo que permite retirar todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros"
    
    def retirarTodo(self):
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldoAhorros())
        self.__cuentaCorriente.RetirarSaldo(self.__cuentaCorriente.DarSaldoCorriente())
    
    __method__="duplicarAhorro"
    __parameter__="Monto"
    __returns__="Ninguna"
    __Description__="Metodo que permite duplicar la cantidad de dinero que hay en la cuenta de ahorros"
        
    def duplicarAhorro(self,monto):
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldoAhorros())