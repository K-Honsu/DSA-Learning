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


# print(count_word_frequency(
#     ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))


# arr = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# for arry in arr:
#     print(arry[arr])


def merge_dicts(dict1, dict2):
    new_dict = dict1.copy()
    for key, value in dict2.items():
        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value
    return new_dict


# print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))


# def max_value_key(my_dict):
#     number = 0
#     max_key = None
#     for key, value in my_dict.items():
#         if value > number:
#             number = value
#             max_key = key
#     return max_key


def max_value_key(my_dict):
    max_value = float('-inf')
    max_key = None
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


print(max_value_key({'a': 5, 'b': 9, 'c': 2}))


def max_value_key1(my_dict):
    return max(my_dict, key=my_dict.get)


# print(max_value_key1({'a': 5, 'b': 9, 'c': 2}))


def reverse_dict(my_dict):
    return {value: key for (key, value) in my_dict.items()}


# print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))


def check_same_frequency(list1, list2):
    for i in list1:
        if list1.count(i) != list2.count(i):
            return False
    return True


# print(check_same_frequency([1, 2, 3, 2, 1], [3, 1, 2, 1, 3]))
