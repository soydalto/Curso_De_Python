#si el modulo estuviera dentro de una carpeta en la misma ruta 
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("c:\\Users\\Rainbow 6\\Desktop\\Curso de Python DALTO\\funciones_buenas")

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))