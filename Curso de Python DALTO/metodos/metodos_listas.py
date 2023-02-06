
#Creando una lista con list()
lista = list([34,56,23,True,False])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"TOMA MAMA")

#agregando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asì sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(56)