from Cliente import Cliente
from ListaShucos import ListaShucos

class Orden:
    def __init__(self, cliente=Cliente(), shucos=ListaShucos()) -> None:
        self.__cliente=cliente
        self.__shucos=shucos
        self.__tiempo=shucos.getTiempo()


    def getCliente(self):
        return self.__cliente

    def getShucos(self):
        return self.__shucos

    def getTiempo(self):
        return self.__tiempo
