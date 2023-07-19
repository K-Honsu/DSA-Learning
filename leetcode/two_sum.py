import numpy as np


def returnIndices(arr, target):
    if len(arr) == 0:
        return f'Array is empty'
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                return f'Found target at index {[i,j]}'
    return -1

# time complexity = O(n^2)


# print(returnIndices([2, 6, 3, 9, 11], 9))
# let's try with obj


def returnIndexWithObj(arr, target):
    if len(arr) == 0:
        return f'Array is empty'
    store = {}
    for index, number in enumerate(arr):
        diff = target - number
        if diff in store:
            return [store[diff], index]
        store[number] = index
    return -1

# time complexity = O(n)


# print(returnIndexWithObj([1], 9))


def maxProductOfTwoIntegers(arr):
    arr.sort(reverse=True)
    return arr[0] * arr[1]


# print(maxProductOfTwoIntegers([2, 6, 3, 9, 11]))


# def secondMaxProductOfIntegers(arr):
#     first_max = 0
#     second_max = 0
#     for i in range(len(arr)):
#         if arr[i] > first_max:
#             first_max = arr[i]
#         elif arr[i] > second_max and arr[i] < first_max:
#             second_max = arr[i]
#     print(first_max, second_max)
#     return first_max * second_max


# print(secondMaxProductOfIntegers([2, 6, 3, 9, 11]))


def secondMaxProductOfIntegers(arr):
    first_max = 0
    second_max = 0

    for i in range(len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            print(second_max)
            first_max = arr[i]
            print(first_max)
        elif arr[i] > second_max and arr[i] < first_max:
            second_max = arr[i]

    # print(first_max, second_max)
    return first_max * second_max


print(secondMaxProductOfIntegers([2, 6, 3, 9, 11]))


def middle(lst):
    return [lst[1:-1]]


print(middle([1, 2, 3, 4]))


def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total


print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')

    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)


def remove_duplicates(arr):
    obj = {}
    for index, value in enumerate(arr):
        if value in obj:
            continue
        obj[value] = index
    return list(obj.keys())


print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
