from Shuco import Shuco

class ShucoCostilla(Shuco):
    def __init__(self, cantidad=None) -> None:
        super().__init__(cantidad)
        self.__tiempo=6

    def getTiempo(self):
        return self.__tiempo