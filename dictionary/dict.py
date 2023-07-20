'''
A dictionary is a collection which is unordered, changeable and indexed ,
mutable collection of key, value pairs, where each unique key matches the value
they are also key: value pairs
to acess a value in the dictionary, we do name of dictionary[key]
'''
# creating a dictionary
my_dict1 = dict()
print(my_dict1)  # -> time complexity is O(1)
my_dict2 = {}
print(my_dict2)  # -> time complexity is O(1)

eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)  # time complexity is O(n)
eng_sp2 = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng_sp2)  # time complexity is O(n)

eng_sp3 = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
eng_sp3_dict = dict(eng_sp3)
print(eng_sp3_dict)  # time complexity is O(n)


# hast tables is a way of doing key-value lookups. You store the values in an array,
# and then use hash function to find the index of the array cellthat corresponds to key-value pair


# update/add pairs in a dict
myDict = {'name': 'Eddy', 'age': 26}
# to update we do
myDict['age'] = 27
print(myDict)
# we can also use it to add key:value pair to the dict, eg
myDict['address'] = 'London'
# this line above, is checking if the key exist in the current dict, if not, then it adds both the key:value to the dict
print(myDict)


# traverse/loop a dict ->
def traverseDict(dic):
    for key in dic:
        print(key, dic[key])


traverseDict(myDict)

for key, value in myDict.items():
    print(key, value)

# searching through a value in a dict


def searchDict(dic, element):
    for key, value in dic.items():
        if value == element:
            print((key, value))
    return -1


searchDict(myDict, 'Eddy')
