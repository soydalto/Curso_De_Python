#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True: 
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepción, pedirle que reingrese los datos
        except ValueError as e: 
            print("Te pedì un numero salame, no te hagas el gracioso")
            print(f"ERROR: {e}")
        #si todo salio bien terminamos el bucle
        else: 
            break
        #el finally se ejecuta siempre
        finally: 
            print("Esto se ejecuta siempre")
    
    #mostrando el resultado
    return resultado

print(sumar_dos())