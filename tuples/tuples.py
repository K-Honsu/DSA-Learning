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