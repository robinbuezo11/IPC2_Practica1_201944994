from Shuco import Shuco

class ShucoSalchica(Shuco):
    def __init__(self, cantidad=0) -> None:
        super().__init__(cantidad)
        self.__tiempo=2
        self.__tipo='Salchicha'

    def getTiempo(self):
        return self.__tiempo

    def getTipo(self):
        return self.__tipo