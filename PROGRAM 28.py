import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
df=pd.read_csv("Car.csv")
plt.figure(figsize=(10,6))
plt.scatter(df['mpg'],df['horsepower'])
plt.xlabel('MPG')
plt.ylabel('Horsepower')
plt.title("Multivariate Scatterplot")
plt.grid(True)
plt.show()
scatter_matrix(df,alpha=0.8,figsize=(10,10),diagonal='hist')
plt.suptitle("Scatter Plot Matrix")
plt.show()
