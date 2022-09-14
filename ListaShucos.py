from NodoShuco import NodoShuco

class ListaShucos:
    def __init__(self, primero=NodoShuco()) -> None:
        self.__primero=NodoShuco()

    def insertar(self, shuco):
        if self.__primero.getShuco().getCantidad() == None:
            self.__primero=NodoShuco(shuco=shuco)
            return
        
        nodoaux=self.__primero
        while nodoaux.getSiguiente():
            nodoaux=nodoaux.getSiguiente()
        
        nodoaux.setSiguiente(NodoShuco(shuco=shuco))