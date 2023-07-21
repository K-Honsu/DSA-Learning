import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Marid']

city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)

new_temps = {key: value for (key, value) in city_temps.items() if value > 25}
print(new_temps)



