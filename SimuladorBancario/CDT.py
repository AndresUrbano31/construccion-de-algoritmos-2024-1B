__author__ = "Benjamin Andres Urbano Zuñiga"
__license__ = "GPL"
__version__ =  "1.0.0"
__email__= "benjamin.urbano@campusucc.edu.co"

class Cdt:
    def __init__(self, saldoCdt, nuevoInteres):
        """Inicializa el cliente con saldo de CDT e interés."""
        self._interes = nuevoInteres
        self._saldoCdt = saldoCdt

    def ValorInteres(self, nuevoInteres):
        """Método que retorna el valor del interés."""
        self._interes = nuevoInteres
        return self._interes

    def ValorInvertido(self, nuevoValor):
        """Método que retorna el saldo del CDT."""
        self._saldoCdt += nuevoValor
        return self._saldoCdt