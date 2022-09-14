from Shuco import Shuco

class ShucoChorizo(Shuco):
    def __init__(self, cantidad=None) -> None:
        super().__init__(cantidad)
        self.__tiempo=3

    def getTiempo(self):
        return self.__tiempo