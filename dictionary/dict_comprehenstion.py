import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Marid']

city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)

new_temps = {key: value for (key, value) in city_temps.items() if value > 25}
print(new_temps)


# def count_word_frequency(words):
#     new_dict = {}
#     for i in words:
#         if i in new_dict:
#             new_dict[i] += 1
#         new_dict[i] = 1
#     return new_dict

def count_word_frequency(words):
    new_dict = {}
    for word in range(len(words)):
        print(words[word])
        if words[word] in new_dict:
            new_dict[words[word]] += 1
        else:
            new_dict[words[word]] = 1
    return new_dict


print(count_word_frequency(
    ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))


# arr = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# for arry in arr:
#     print(arry[arr])
