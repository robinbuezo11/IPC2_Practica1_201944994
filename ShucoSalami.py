from Shuco import Shuco

class ShucoSalami(Shuco):
    def __init__(self, cantidad=0) -> None:
        super().__init__(cantidad)
        self.__tiempo=1.5
        self.__tipo='Salami'

    def getTiempo(self):
        return self.__tiempo

    def getTipo(self):
        return self.__tipo