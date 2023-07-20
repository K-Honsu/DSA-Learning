# in operator -> works with keys and not values
myDict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(3 in myDict)
# but to check if it exist in the values, we can use the values() method
print('five' in myDict.values())

# len()
print(len(myDict))

# all() -> check


# sorted() -> returns the sorted format for all keys to an array
print(sorted(myDict))
