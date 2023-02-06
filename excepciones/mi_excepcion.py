#creando mi propia excepción personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        

#Lanzando mi propia excepcion
#raise MiExcepcion("Jajajajaja, persona poco culta")

#manejandola
try:
    raise MiExcepcion("Jajajajaja, persona poco culta")
except:
    print("Como vas a cometer ese error?")
