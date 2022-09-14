from Shuco import Shuco

class ShucoSalchica(Shuco):
    def __init__(self, cantidad=None) -> None:
        super().__init__(cantidad)
        self.__tiempo=2

    def getTiempo(self):
        return self.__tiempo