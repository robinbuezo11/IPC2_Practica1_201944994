from Shuco import Shuco

class ShucoSalami(Shuco):
    def __init__(self, cantidad=None) -> None:
        super().__init__(cantidad)
        self.__tiempo=1.5

    def getTiempo(self):
        return self.__tiempo