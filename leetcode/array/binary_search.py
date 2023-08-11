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
    if len(arr) == 0:
        return 'Empty'
    while first <= last:
        midpoint = (first + last) // 2
        if value == arr[midpoint]:
            return True
        elif value > arr[midpoint]:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return False
        
print(withoutRecursionForBinarySearch([1,2,3,4,5,6,9], 9))
arr1= [1,49,66,90]
arr2= [2,99,7,8]
arr1.extend(arr2)
# srt = sorted(arr1)
# print(srt)
# print()
def mergeSortedArray(nums1:list, nums2:list):
    nums1.extend(nums2)
    k = 0
    for i in range(len(nums1)):
        minn = i
        for j in range(i+1, len(nums1)):
            if nums1[j] < nums1[minn]:
                minn = j
        nums1[i], nums1[minn] = nums1[minn], nums1[i]
    return nums1
            

print(mergeSortedArray([1,49,66,90],[2,99,7,8]))
arr= ['bill','soji', 'susan']
arrr= ['08023358137', '111-111-111', None]
x = [[name,phone] for name,phone in zip(arr,arrr)]
# print(x)

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# # Initialize pointers
# pointer1 = 0
# pointer2 = 0

# # Iterate through both lists using a while loop
# while pointer1 < len(list1) and pointer2 < len(list2):
#     element1 = list1[pointer1]
#     element2 = list2[pointer2]
    
#     # Process or compare the elements here
#     # For example, print them
#     print("Element from list1:", element1)
#     print("Element from list2:", element2)
    
#     # Move the pointers to the next elements
#     pointer1 += 1
#     pointer2 += 1
