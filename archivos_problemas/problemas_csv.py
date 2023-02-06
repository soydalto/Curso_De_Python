#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#remplazando los datos "dalto" por "Maestro"
df['apellido'].replace("dalto","maestro",inplace=True)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")





