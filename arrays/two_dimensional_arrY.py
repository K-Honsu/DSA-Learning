import numpy as np

# good for two dimensional array
twoArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5],
                    [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoArray)

# insertion in two dimensional array
# nb: if axis is set to 1, it will add to column, otherwise 0 will set to row
newTwoDArray = np.insert(twoArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# Accessing elements in two dimensional array
# remember two dimensional array, has two index,
# so we can access it by getting both index: row x index
print(newTwoDArray[2][2])
# in the above, first index is the row while second index is the column

# in function


def accessTwoDarray(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Index out of range')
    else:
        print(array[rowIndex][colIndex])


accessTwoDarray(newTwoDArray, 2, 2)


def traverseTwoDarray(arr):
    for i in range(len(arr)):
        for k in range(len(arr[0])):
            print(arr[i][k])


traverseTwoDarray(twoArray)


def searchTwoDArray(arr, value):
    for i in range(len(arr)):
        for k in range(len(arr[0])):
            if arr[i][k] == value:
                return f'The value is at index {i} {k}'
    return 'Value not found'


# print(searchTwoDArray(newTwoDArray, 0))


# def newSearchTwoDArray(arr, value):
#     for i in range(len(arr)):
#         for k in range(len(arr[0])):
#             if value in arr[i][k]:
#                 return True
#     return False


# print(newSearchTwoDArray(twoArray, 14))


# deleting from an 2d array
new_output = np.delete(twoArray, 0, axis=0)
# print(new_output)
