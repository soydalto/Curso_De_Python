import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")

#creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#mostrando el grafico
plt.show()
