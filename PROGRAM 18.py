temperature_data={
    'City1':[22,25,23,21,24,26,28,27,25,23,22,21],
    'City2':[25,27,26,24,25,27,29,28,26,24,25,24],
    'City3':[23,24,22,21,22,23,25,24,23,22,21,20],
    'City4':[27,28,27,26,27,28,30,29,27,26,27,26]}
city_means={}
for city,temperatures in temperature_data.items():
    city_means[city]=sum(temperatures)/len(temperatures)
import statistics
city_stds={}
for city,temperatures in temperature_data.items():
    city_stds[city]=statistics.stdev(temperatures)
highest_range_city=None
highest_range=0
for city,temperatures in temperature_data.items():
    temperature_range=max(temperatures) - min(temperatures)
    if temperature_range>highest_range:
        highest_range_city=city
        highest_range=temperature_range
most_consistent_city=None
lowest_std=float('inf')
for city,std in city_stds.items():
    if std < lowest_std:
        most_consistent_city=city
        lowest_std=std
print("Mean temperatures:")
for city,mean in city_means.items():
    print(f"{city}:{mean:.2f}")
print("\nStandard deviations:")
for city,std in city_stds.items():
    print(f"{city}:{std:.2f}")
print("\nCity with the highest temperature range:",highest_range_city)
print("Temperature range:",highest_range)
print("\nCity with the most consistent temperature:",most_consistent_city)
print("Standard deviation:",lowest_std)
