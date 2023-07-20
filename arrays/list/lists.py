# traversing a list
shopping_list = ['Milk', 'Cheese', 'Groudnut']

for i in range(len(shopping_list)):
    shopping_list[i] += '+'
    print(shopping_list[i], i)


for i in shopping_list:
    print(i)

# inserting element in a list
# there are three methods we can use namely, insert(), append() or extend()

# intert() method, takes in the index of where we want to insert as well as the value

myList = [1, 2, 3, 4, 5, 6]
print(myList)
myList.insert(0, 11)
print(myList)

# append() method, this only adds an element to the end of the list
myList.append(30000)
print(myList)

# extend() method, allows us to add a list to a pre-existing list
newArray = [7, 8, 9, 10]
myList.extend(newArray)
print(myList)

letter_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(letter_list[1:])
# we can also update multiple elements in alist with the slice operator
letter_list[0:2] = ['x', 'y']
print(letter_list)

# deleting elements in a list - pop(), remove(), delete()
# take index and if it doesn't pass index, it delete the last element in the list
letter_list.pop(1)

# del method -> this also takes in the index of what we want to delete, and we use square bracket, we can slice elements
del letter_list[0]
print(letter_list)

# remove() method, takes the value and not the index
letter_list.remove('f')
print(letter_list)

# searching for elements in list
new_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 500

# if target in new_list:
#     print(f'{target} in list')
# else:
#     print(f'{target} not found')

# linear search


def linearSearch(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return f'{target} is located at index {i}'
    return -1


print(linearSearch(new_list, 200))


def missing_number(arr, n):
    if n <= 0:
        return 'Number must be grater than 0'
    # Calculate the sum of integers from 1 to n using the arithmetic series formula
    expected_sum = (n * (n + 1)) // 2

    # Calculate the actual sum of elements in the array
    actual_sum = sum(arr)

    # Find the missing number by subtracting the actual sum from the expected sum
    missing_num = expected_sum - actual_sum

    return missing_num


print(missing_number([1, 2, 3, 4, 6], -22))


def returnIndexOfTarget(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return -1


# print(returnIndexOfTarget([2, 6, 3, 9, 11], 9))

def returnIndexWithObj(arr, target):
    prevMap = {}
    for index, number in enumerate(arr):
        print(index, number)
        diff = target - number
        if diff in prevMap:
            print(prevMap[diff])
            return [prevMap[diff], index]
        prevMap[number] = index

    return -1


print(returnIndexWithObj([2, 6, 3, 9, 11], 9))
ken = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(ken)//2)
print(ken[:2])



def binarySearch(arr, value):
    middle = len(arr) // 2
    if arr[middle] == value:
        return True
    elif arr[middle] < value:
        return binarySearch(arr[middle+1:], value)
    else:
        return binarySearch(arr[:middle], value)


print(binarySearch(ken, 8))
