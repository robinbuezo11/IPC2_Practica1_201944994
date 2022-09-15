from colorama import Fore

class Shuco:
    def __init__(self, cantidad=0) -> None:
        self.__cantidad=int(cantidad)
        self.__tipo='Shuco'
        self.__tiempo=1

    def getCantidad(self):
        return self.__cantidad

    def setCantidad(self, cantidad):
        try:
            self.__cantidad=int(cantidad)
        except Exception as e:
            print(Fore.RED + f'{e}')
    
    def getTipo(self):
        return self.__tipo

    def getTiempo(self):
        return self.__tiempo
