import pandas as pd
data={'Product':['Product A','Product B','Product C','Product D','Product E','Product A','Product B','Product C','Product D','Product E'],
      'Quantity':[10,20,30,40,50,15,25,35,45,55]}
df=pd.DataFrame(data)
product_quantity=df.groupby('Product')['Quantity'].sum()
product_quantity_sorted=product_quantity.sort_values(ascending=False)
top_5_products=product_quantity_sorted.head(5)
print(top_5_products)
