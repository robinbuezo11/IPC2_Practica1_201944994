from Shuco import Shuco

class ShucoChorizo(Shuco):
    def __init__(self, cantidad=0) -> None:
        super().__init__(cantidad)
        self.__tiempo=3
        self.__tipo='Chorizo'

    def getTiempo(self):
        return self.__tiempo

    def getTipo(self):
        return self.__tipo