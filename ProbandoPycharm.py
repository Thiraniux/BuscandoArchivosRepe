import os
import ventanarutas

directorio = "C:/Users/enri_"
archivos = os.listdir(directorio)

def __archivosdir__():
    count = 0
    nombrecarpetas = []
    listax = []
    for item in archivos:
        if item.startswith(".") or (item.__len__()>=15):
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
        direcc = directorio+'/'+item
        #print(direcc)

listado = __archivosdir__()
__buscandoraiz__(listado)

