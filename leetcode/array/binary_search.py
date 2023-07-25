# implementing a binary search algorithm using recursion
def recursiveBinarySearch(arr, value):
    # if len(arr) <= 0:
    #     return 'len of array is less than 1 or array is empty'
    midpoint = len(arr) // 2
    if value == midpoint:
        return f'the value is located at midpoint value which is {arr[midpoint]}'
    elif value > midpoint:
        return recursiveBinarySearch(arr[midpoint+1:], value)
    elif value < midpoint:
        return recursiveBinarySearch(arr[:midpoint],value)
    return f'value not found in the array'
        
    
# print(recursiveBinarySearch([1,2,3,4,9,4,5,6], 20))

# can you try without using the recursion
def withoutRecursionForBinarySearch(arr, value):
    first = 0
    last = len(arr) - 1
    while first <= last:
        midpoint = (first + last)//2
        if arr[midpoint] == value:
            return f'value found in array at {midpoint}'
        elif arr[midpoint] > value:
            first = midpoint + 1
        else:
            last - midpoint - 1
    return None
        
print(withoutRecursionForBinarySearch([1,2,3,4,9,4,5,6], 6))
