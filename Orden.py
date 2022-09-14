from Cliente import Cliente
from ListaShucos import ListaShucos

class Orden:
    def __init__(self, cliente=Cliente(), shucos=ListaShucos()) -> None:
        self.__cliente=cliente
        self.__shucos=shucos

    def getCliente(self):
        return self.__cliente

    def getShucos(self):
        return self.__shucos

