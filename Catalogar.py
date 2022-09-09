def catalogar(lista, ruedas = 0):
    if ruedas == 0:
        for i in lista:
            print(i)
    else:
        suma = 0
        for i in lista:
            if i.get_ruedas() == ruedas:
                suma +=1

        print(f'Se han encontrado {suma} vehiculos con {ruedas} ruedas')
