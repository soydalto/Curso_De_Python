#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo= open("archivos\\texto_de_dalto.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo.read()

#leer una sola linea
#linea = archivo.readline()

#leer linea por linea
lineas = archivo.readlines()

#cerrar el archivo
archivo.close()


print(lineas)