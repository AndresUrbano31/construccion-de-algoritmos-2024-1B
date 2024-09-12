__author__ = "Benjamin Andres Urbano Zuñiga"
__license__ = "GPL"
__version__ =  "1.0.0"
__email__= "benjamin.urbano@campusucc.edu.co"

from CuentaCorriente import cuentaCorriente
from Cdt import cdt
from CuentaCorriente import cuentaAhorros
class Cliente: 
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    nombre =""
    cedula = 1085284611

    """#----------------------------------------------------------------
    # Asociacion = traer una class que esta en otro archivo 
    ----------------------------------------------------------------#"""
    cuentaCorriente()
    cuentaAhorros()
    cdt()
    

