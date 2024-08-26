import os
import ventanarutas

directorio = ventanarutas.ruta
archivos = os.listdir(directorio)

def __archivosdir__(archivos):
    count = 0
    nombrecarpetas = []
    listax = []
    for item in archivos:
        if item.startswith(".") or (item.__len__()>=15 or item.startswith("$")):
            listax.append(item)
            count +=1

        else:
            #print(item + " \n")
            nombrecarpetas.append(item)
    #print(listado)
    #print(listax)
    print("total de elementos sistema no incluidos",count)
    return nombrecarpetas



def __buscandoraiz__(lista):
    for item in lista:
        direcc = directorio+item
        print(direcc)

listado = __archivosdir__(archivos)
__buscandoraiz__(listado)

