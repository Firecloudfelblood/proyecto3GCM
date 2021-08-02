def respuesta_pares(arr):
    arr = remover(arr)

    if arr == '':
        return 'Helado es el vacio'
    else:
        return arr


def remover(lista):
    if not len(lista) == 1:
        go = True
        while go:
            for x in range(len(lista) - 1):
                if lista[x] == lista[x + 1]:
                    lista = lista[0: x:] + lista[x + 2::]
                    if len(lista) < 4:
                        go = False
                    break

    return lista
