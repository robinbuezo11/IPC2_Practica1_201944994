from colorama import Fore

class Shuco:
    def __init__(self, cantidad=None) -> None:
        try:
            self.__cantidad=int(cantidad)
        except Exception as e:
            print(Fore.RED + f'{e}')

    def getCantidad(self):
        return self.__cantidad

    def setCantidad(self, cantidad):
        try:
            self.__cantidad=int(cantidad)
        except Exception as e:
            print(Fore.RED + f'{e}')
