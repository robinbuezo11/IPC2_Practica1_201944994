from Shuco import Shuco

class ShucoLonganiza(Shuco):
    def __init__(self, cantidad=0) -> None:
        super().__init__(cantidad)
        self.__tiempo=4
        self.__tipo='Longaniza'

    def getTiempo(self):
        return self.__tiempo

    def getTipo(self):
        return self.__tipo