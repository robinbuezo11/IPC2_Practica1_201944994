from Shuco import Shuco

class ShucoLonganiza(Shuco):
    def __init__(self, cantidad=None) -> None:
        super().__init__(cantidad)
        self.__tiempo=4

    def getTiempo(self):
        return self.__tiempo