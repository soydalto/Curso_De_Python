import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} USD")

#mostrando el grafico
plt.show()
