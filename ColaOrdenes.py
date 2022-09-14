from colorama import Fore
from NodoOrden import NodoOrden

class ColaOrdenes:
    def __init__(self, primero=NodoOrden()) -> None:
        self.__primero=primero

    def encolar(self, orden):
        if self.__primero.getOrden().getCliente().getNombre() == None:
            self.__primero=NodoOrden(orden=orden)
            return
        
        nodoaux=self.__primero
        while nodoaux.getSiguiente():
            nodoaux=nodoaux.getSiguiente()
        
        nodoaux.setSiguiente(NodoOrden(orden=orden))    

    def desencolar(self):
        if self.__primero.getOrden().getCliente().getNombre() == None:
            print(Fore.RED + 'No existe ninguna orden')
            return
        
        desencolado=self.__primero
        self.__primero=self.__primero.getSiguiente()
        desencolado.setSiguiente(None)
        return desencolado