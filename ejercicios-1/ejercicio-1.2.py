
#le pedimos al usuario que nos diga una frase (o varias)
frase = input("Decime una frase y te calculo cuanto tardarìas si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde màs de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedì un testamento")
    
#Calculamos cuanto tardaría en decir las palabras y se lo decimos    
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarìas {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo dirìa en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos')

