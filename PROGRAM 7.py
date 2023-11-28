import numpy as np
house_data = np.array([
    [3, 1500, 25000],
    [4, 2000, 30000],
    [5, 2500, 35000],
    [2, 1200, 20000],
    [5, 3000, 40000],
])
filtered_data = house_data[house_data[:, 0] > 4]
average_price = np.mean(filtered_data[:, 2])
print("Average sale price of houses with more than four bedrooms:", average_price)
