import numpy as np
fuel_efficiency=np.array([30,35,25,40,32])
fuel_efficiency_model_A=30
fuel_efficiency_model_B=40
average_fuel_efficiency=np.mean(fuel_efficiency)
percentage_improvement=((fuel_efficiency_model_B - fuel_efficiency_model_A)/fuel_efficiency_model_A)*100
print("\nAverage fuel efficiency:",average_fuel_efficiency)
print("Percentage improvement:",percentage_improvement)
