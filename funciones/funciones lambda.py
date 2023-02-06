numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#creando funcion comun que diga si es par o no
#def es_par(num):
#    if (num%2==1):
#        return True
    
#usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))
