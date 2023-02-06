#importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu

#creamos las variables con los saludos
saludo = saludar_normal("Lucas")
saludo_raro = saludar_como_coscu("Fran")

#mostramos los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)