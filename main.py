from lanzador import *
if __name__ == '__main__':
    print('Nuestros vehñiculos son los siguientes:\n\n')
    catalogar(lista)

    n = int(input('\n\nFiltro por numero de ruedas:'))
    catalogar(lista, n)
