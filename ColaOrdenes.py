import os
from colorama import Fore
from NodoOrden import NodoOrden
from Orden import Orden

class ColaOrdenes:
    def __init__(self, primero=NodoOrden()) -> None:
        self.__primero=primero
        self.__contadorordenes=1
        self.__ordenesactuales=0

    def encolar(self, orden=Orden()):
        nuevaorden=orden

        if self.__primero.getOrden().getCliente().getNombre() == None:
            self.__primero=NodoOrden(orden=nuevaorden)
            self.__contadorordenes+=1
            self.__ordenesactuales+=1
            return
        
        nodoaux=self.__primero
        while nodoaux.getSiguiente():
            nuevaorden.setTiempoCola(nuevaorden.getTiempoCola()+nodoaux.getOrden().getTiempo())
            nodoaux=nodoaux.getSiguiente()
        nuevaorden.setTiempoCola(nuevaorden.getTiempoCola()+nodoaux.getOrden().getTiempo())
        
        nodoaux.setSiguiente(NodoOrden(orden=nuevaorden)) 
        self.__contadorordenes+=1
        self.__ordenesactuales+=1  

    def desencolar(self):
        if self.__primero.getOrden().getCliente().getNombre() == None:
            print(Fore.RED + 'No existe ninguna orden')
            return
        
        desencolado=self.__primero
        if self.__primero.getSiguiente():
            self.__primero=self.__primero.getSiguiente()
        else:
            self.__primero=NodoOrden()
        desencolado.setSiguiente(None)
        self.__ordenesactuales-=1
        return desencolado

    def toString(self):
        string=Fore.MAGENTA + '--------------COLA--------------\n'
        if self.__primero.getOrden().getCliente().getNombre() == None:
            string=Fore.CYAN + 'No hay ninguna orden en cola'
            return string
        
        nodoaux=self.__primero
        contador=self.__contadorordenes-self.__ordenesactuales
        while nodoaux:
            orden=Fore.WHITE + f'\nOrden No. {contador}\n{nodoaux.getOrden().getCliente().getNombre()}\n{nodoaux.getOrden().getShucos().toStringWhithColor()}Tiempo: {nodoaux.getOrden().getTiempo()} min\nTiempo en Cola: {nodoaux.getOrden().getTiempoCola()}\n'
            string += orden
            nodoaux=nodoaux.getSiguiente()
            contador+=1
        
        return string

    def graficar(self):
        text = 'digraph {node[shape=plain style=filled pencolor="#00000" color="#3ADEFF" fontname="Helvetica,Arial,sans-serif"]edge[dir=back] '
        direccion = ''
        contador=self.__contadorordenes-self.__ordenesactuales

        if self.__primero.getOrden().getCliente().getNombre() == None:
            text += f'Orden{contador}[label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Cola vacia</b></td></tr></table>>]'
        else:
            nodoaux=self.__primero

            while nodoaux:
                if nodoaux.getSiguiente():
                    shucos=nodoaux.getOrden().getShucos().toString().replace("\n","<br/>")
                    text += f'Orden{contador}[label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Orden {contador}</b></td></tr>'
                    text += f'<tr><td>{nodoaux.getOrden().getCliente().getNombre()}<br/>{shucos}Tiempo: {nodoaux.getOrden().getTiempo()}<br/>Tiempo en Cola: {nodoaux.getOrden().getTiempoCola()}</td></tr></table>>]'
                    direccion += f'Orden{contador}->'
                    nodoaux=nodoaux.getSiguiente()
                    contador+=1
                else:
                    shucos=nodoaux.getOrden().getShucos().toString().replace("\n","<br/>")
                    text += f'Orden{contador}[label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Orden {contador}</b></td></tr>'
                    text += f'<tr><td>{nodoaux.getOrden().getCliente().getNombre()}<br/>{shucos}Tiempo: {nodoaux.getOrden().getTiempo()}<br/>Tiempo en Cola: {nodoaux.getOrden().getTiempoCola()}</td></tr></table>>]'
                    direccion += f'Orden{contador}'
                    nodoaux=nodoaux.getSiguiente()
                    contador+=1
        
        text+=direccion
        text+='}'
        file = open("./cola.dot","w+")
        file.write(text)
        file.close()
        os.system(f'dot -Tpng cola.dot -o cola.png')