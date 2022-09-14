from Shuco import Shuco

class NodoShuco:
    def __init__(self, shuco=Shuco(), siguiente=None) -> None:
        self.__shuco=shuco
        self.__siguiente=siguiente

    def getShuco(self):
        return self.__shuco

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente