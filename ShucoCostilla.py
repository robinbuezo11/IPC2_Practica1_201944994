from Shuco import Shuco

class ShucoCostilla(Shuco):
    def __init__(self, cantidad=0) -> None:
        super().__init__(cantidad)
        self.__tiempo=6
        self.__tipo='Costilla'

    def getTiempo(self):
        return self.__tiempo

    def getTipo(self):
        return self.__tipo