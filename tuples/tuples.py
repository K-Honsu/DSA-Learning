# these are immutable sequence of python objects, they are also comparable and hashable
# an object is said to be hashable if it has a value that remains the same forever
tupel = ('a', 'b', 'c', 'd', 'e')
print(tupel)
# when creating single element tuple, we have to add the comma at the end, to tell the intepreter that is a tuple, eg
newTuple = ('a',)  # if not added, it becomes a string
print(newTuple)
# we can also use the tuple keyword
newTuple1 = tuple('abcde')
print(newTuple1)

# accessing elements with tuples using []
print(tupel[1])
# we can also use slice operator to slice elements


# Traversing elements in tuple
for i in tupel:
    # print(i)
    pass
for i in range(len(tupel)):
    # print(tupel[i])
    pass

# Searching for elements in tuple
# method 1 -> using "in" operator
print('b' in tupel)
# method 2 -> using "index" method -> this is to get the index number
print(tupel.index('c'))
# method 3 -> using function
def searchTuple(tup, element):
    for i in range(len(tup)):
        if tup[i] == element:
            return f"The element {element} is located at index {i}"
    return f"The element {element} was not found"

print(searchTuple(tupel, 'c'))