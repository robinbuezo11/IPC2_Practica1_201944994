from Orden import Orden

class NodoOrden:
    def __init__(self, orden=Orden(), siguiente=None) -> None:
        self.__orden=orden
        self.__siguiente=siguiente

    def getOrden(self):
        return self.__orden

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente