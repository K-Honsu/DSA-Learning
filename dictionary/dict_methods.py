# clear() -> deletes all elements from the dictionary
myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# myDict.clear()
# print(myDict)

# copy() -> returns a copy of the original dictionary, without modifying the original dictionary
dic = myDict.copy()
# print(myDict)
# print(dic)

# fromkeys() -> creates a new dict from given sequence of elements provided, takes in two parameters,
# the sequence of keys and the value, note, if no value is assigned, None value will be automatically assigned to it
new_dict = {}.fromkeys([1, 2, 3, 4], 0)
print(new_dict)
new_dict1 = {}.fromkeys([1, 2, 3, 4])
print(new_dict1)

# get() -> returns the value of the specified key in the dictionary if the key is in the dictionary,
# it takes in two parameters, which is the key and the value, if the key is not in the dic, the value will be returned,
# also, if the key is not in the dictionary and the value parameter is not passed, then it returns None
print(myDict.get('age'))  # None
print(myDict.get('age', 27))  # 27
print(myDict.get('one'))  # uno


# items() -> returns key, value pair of dict (tuple)
print(myDict.items())

# keys() -> returns all keys in the dict (array)
print(myDict.keys())

# popitem() -> returns an arbitrary pair from the dic and then deletes it from the dictionary
print(myDict.popitem())

# setDefault() -> takes in the key and the value, if the key is found in the dict, it returns the value of the key,
# else, it insert the key as well as the value passed into it
print(myDict.setdefault('one', 'two'))  # uno
print(myDict.setdefault('four', 'quarte'))  # four:quarte
print(myDict)

# pop() -> takes in key and value as params and deletes the key and value from the dict, if key not found, it raise valueError
myDict.pop('four')
print(myDict)

# update() -> updates the dictionary with the elements from another dict
new_dict5 = {'a': 1, 'b': 2, 'c': 3}
myDict.update(new_dict5)
print(myDict)
