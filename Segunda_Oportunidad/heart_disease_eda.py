from ucimlrepo import fetch_ucirepo 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(
        {
            "chetos":[
                "flamin hot",
                "torciditos",
                "bola",
                "pizza",
                "azules",
                "verdes",
                "rojos",
                ]

            }
        )

# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata
print(heart_disease.metadata) 
  
# variable information 
print(df.head(5)) 

df.shape
df.dtypes 
df.info()
df.isnull().sum()
df.describe()

target_counts = df['chetos'].valuea_counts()

plt.figure(figsize=(5,1))

target_counts.plot(kind='bar', color=['#4C72B0', '#C44E52'])

plt.title('Distribucion de la clase objetivo (target: 0 vs 1)')
plt.xlabel('Clase')
plt.ylabel('Cantidad de registros')
plt.xtrick([0,1],['Clase 0', 'Clase 1', rotation==0])
plt.show()

target_counts = df['chetos'].value_counts()

# Configuración del tamaño
plt.figure(figsize=(7, 7))

# Gráfica utilizando Matplotlib con porcentajes
plt.pie(target_counts,
        labels=['Clase 0', 'Clase 1'],
        autopct='%1.1f%%',
        colors=['#4C72B0', '#C44E52'],
        startangle=90,
        explode=(0, 0.05)) # Da un ligero efecto de separación a la segunda rebanada

plt.title('Distribución Proporcional de la Clase Objetivo')
plt.show()

