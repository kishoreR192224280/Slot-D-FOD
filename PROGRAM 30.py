import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Shoe size.csv")
frequency_distribution=df.groupby('shoe_size')["quantity"].sum()
print(frequency_distribution)
plt.figure(figsize=(10,6))
frequency_distribution.plot(kind="bar",color="skyblue")
plt.xlabel('Shoe Size')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Shoe Sizes')
plt.show()
