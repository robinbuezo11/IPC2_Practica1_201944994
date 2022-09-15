from colorama import Fore
from NodoShuco import NodoShuco

class ListaShucos:
    def __init__(self, primero=NodoShuco()) -> None:
        self.__primero=NodoShuco()

    def insertar(self, shuco):
        if self.__primero.getShuco().getCantidad() == 0:
            self.__primero=NodoShuco(shuco=shuco)
            return
        
        nodoaux=self.__primero
        while nodoaux.getSiguiente():
            nodoaux=nodoaux.getSiguiente()
        
        nodoaux.setSiguiente(NodoShuco(shuco=shuco))

    def toStringWhithColor(self):
        string=''
        if self.__primero.getShuco().getCantidad() == 0:
            string=Fore.CYAN + 'No hay ningún shuco'
            return string
        
        nodoaux=self.__primero
        while nodoaux:
            shuco=Fore.CYAN + f'{nodoaux.getShuco().getCantidad()} Shuchos de {nodoaux.getShuco().getTipo()}\n'
            string += shuco
            nodoaux=nodoaux.getSiguiente()
        return string

    def toString(self):
        string=''
        if self.__primero.getShuco().getCantidad() == 0:
            string='No hay ningún shuco'
            return string
        
        nodoaux=self.__primero
        while nodoaux:
            shuco=f'{nodoaux.getShuco().getCantidad()} Shuchos de {nodoaux.getShuco().getTipo()}\n'
            string += shuco
            nodoaux=nodoaux.getSiguiente()
        return string

    def getTiempo(self):
        if self.__primero.getShuco().getCantidad() == 0:
            return 0

        tiempo=0
        nodoaux=self.__primero
        while nodoaux:
            tiempo += nodoaux.getShuco().getCantidad()*nodoaux.getShuco().getTiempo()
            nodoaux=nodoaux.getSiguiente()
        return tiempo