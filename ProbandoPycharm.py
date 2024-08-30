import os
import ventanarutas

directorio = ventanarutas.ruta
archivos = os.listdir(directorio)
listax = []
def archivosdir():
    count = 0
    nombrecarpetas = []
    for item in archivos:
        if item.startswith(".") or (item.__len__()>=15) or item.startswith("$"):
            listax.append(item)
            count +=1
        else:
            #print(item + " \n")
            nombrecarpetas.append(item)
    #print(nombrecarpetas)
    print("total de elementos sistema no incluidos",count)
    return nombrecarpetas



def buscandoraiz(lista):
    for item in lista:
        direcc = directorio+'/'+item
        print(direcc)



