# using the array module to build an array, we do:
import numpy as np
import array
arr = array.array('i')  # ------> O(1) time complexity
# the above lets us create an array of signed integers only
arr = array.array('i', [1, 2, 3, 4, 5])  # ------> O(n) time complexity
print(arr)


# using the numpy module to build an array, we do:
np_array = np.array([], dtype=int)  # ------> O(1) time complexity
# the above lets us create an array of signed integers only
np_array1 = np.array([1, 2, 3, 4, 5])  # ------> O(n) time complexity
# the above crates an array of integers, note: that if we specify the dtype, it is strictly enforced
print(np_array1)


# Insertion in an array
'''
Inserting elements into an array that either be done at the beginning, middle or at the end or even at a specified index
inserting at the beginning of an array is time consuming because we have to shift all the elements to the right # O(n)
Inserting at the end of an array is the easiest because we just have to insert the element at the end of the array # O(1)
while at the middle, we have to shift all the elements to the right of the array # O(n)
'''
# example of inserting at the beginning of an array with array module
arr1 = array.array('i', [1, 2, 3, 4, 5])
# print(arr1)
arr1.insert(0, 6)  # insert takes in 2 arguments, the index and the value
# print(arr1)


def traverse(array):
    for i in range(len(array)):
        print(array[i])


traverse(arr1)


def accessElement(array, index):
    if index >= len(array):
        print('Index out of range')
    else:
        print(array[index])

accessElement(arr1, 0)


def searchElement(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
print('search')
print(searchElement(arr1, 6))
print('search end')



learn = [1, 2, 3, 4, 5, 6, 7, 8]
# print(learn[0])


def deleteElement(array, num):
    for i in range(len(array)):
        if i == num:
            array.remove(i)
    return array


print(deleteElement(learn, 1))


def deleteNum(array, target):
    if target in array:
        array.remove(target)
    return array


print(deleteNum(learn, 8))
