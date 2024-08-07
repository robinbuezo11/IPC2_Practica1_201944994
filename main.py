from colorama import Fore
from Cliente import Cliente
from ColaOrdenes import ColaOrdenes
from ListaShucos import ListaShucos
from Orden import Orden
from ShucoChorizo import ShucoChorizo
from ShucoCostilla import ShucoCostilla
from ShucoLonganiza import ShucoLonganiza
from ShucoSalami import ShucoSalami
from ShucoSalchica import ShucoSalchica

def main():
    ordenes = ColaOrdenes()
    option = 0
    while option != 9:
        print(Fore.BLUE + '\n--------------------MENU-------------------')
        print(Fore.BLUE + '1) Tomar la orden')
        print(Fore.BLUE + '2) Entregar orden')
        print(Fore.BLUE + '8) Datos del desarrollador')
        print(Fore.BLUE + '9) Salir\n')

        try:
            option = int(input(Fore.YELLOW + 'Ingrese el número de la opción que desee '))
        except Exception as e:
            print(Fore.RED + f'{e}')
            option = 0

        if option==1:
            try:
                nombrecliente = input(Fore.YELLOW + '\nNombre del Cliente: ')
                cliente = Cliente(nombre=nombrecliente)

                shucos=ListaShucos()
                option1 = 0
                while option1 != 9:
                    print(Fore.BLUE + '\n--------------------SHUCOS-------------------')
                    print(Fore.BLUE + '1) Salchicha')
                    print(Fore.BLUE + '2) Chorizo')
                    print(Fore.BLUE + '3) Salami')
                    print(Fore.BLUE + '4) Longaniza')
                    print(Fore.BLUE + '5) Costilla')
                    print(Fore.BLUE + '9) Confirmar Orden\n')
                    
                    try:
                        option1 = int(input(Fore.YELLOW + 'Ingrese el número del Shuco que desee '))
                    except Exception as e:
                        print(Fore.RED + f'{e}')
                        option = 0

                    if option1==1:
                        cantidad=input(Fore.YELLOW + 'Ingrese la cantidad de sus shucos de Salchicha: ')
                        shucos.insertar(shuco=ShucoSalchica(int(cantidad)))
                    if option1==2:
                        cantidad=input(Fore.YELLOW + 'Ingrese la cantidad de sus shucos de Chorizo: ')
                        shucos.insertar(shuco=ShucoChorizo(int(cantidad)))
                    if option1==3:
                        cantidad=input(Fore.YELLOW + 'Ingrese la cantidad de sus shucos de Salami: ')
                        shucos.insertar(shuco=ShucoSalami(int(cantidad)))
                    if option1==4:
                        cantidad=input(Fore.YELLOW + 'Ingrese la cantidad de sus shucos de Longaniza: ')
                        shucos.insertar(shuco=ShucoLonganiza(int(cantidad)))
                    if option1==5:
                        cantidad=input(Fore.YELLOW + 'Ingrese la cantidad de sus shucos de Costilla: ')
                        shucos.insertar(shuco=ShucoCostilla(int(cantidad)))
                    
                if shucos.getTiempo()==0:
                    print(Fore.RED + '\nNo seleccionó ningún shuco\n')
                else:
                    ordenes.encolar(orden=Orden(cliente=cliente,shucos=shucos))
                    print(Fore.GREEN + '\nOrden ingresada correctamente\n')
                    print(f'{ordenes.toString()}')
                    ordenes.graficar()

            except Exception as e:
                print(Fore.RED + f'{e}')
        
        if option==2:
            desencolada=ordenes.desencolar()
            if desencolada:
                print(Fore.GREEN + f'\nOrden entregada correctamente \nCliente: {desencolada.getOrden().getCliente().getNombre()}\nOrden:\n{desencolada.getOrden().getShucos().toString()}Tiempo Total: {desencolada.getOrden().getTiempo()+desencolada.getOrden().getTiempoCola()}\n')
            print(Fore.YELLOW + f'{ordenes.toString()}')
            ordenes.graficar()

        if option==8:
            print(Fore.GREEN + '\nDesarrollaror: Robin Omar Buezo Díaz\nCarné: 201944994\nCurso: IPC2\n')

main()