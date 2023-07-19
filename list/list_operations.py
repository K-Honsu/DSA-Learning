# we can concatenate tow list using the +
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a+b
print(c)

# len() -> to get the length of values in the array
print(len(b))

# max() and min(), we can get the maximum as well as minimum value in an array
print(max(b))
print(min(b))

# sum() -> to find sum of all elements in a list
print(sum(b))

# tp get average, we can use sum/len
print(sum(b)//len(b))

# my_list = []
# while True:
#     inp = input('Enter your number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     my_list.append(value)
# average = sum(my_list) / len(my_list)

# print('Average:', average)

# we can convert a string to a list by using the list(), eg
d = 'feranmi'
print(list(d))

# we can also split words into list
e = 'feranmi emmanuel adeyemi'
slp = 'a'
f = e.split(slp)
print(f)
# nb, if i were to do list(e), it will convert each letter and spaces to strings in an array

# list-string, use joint()
print(slp.join(f))

new_arr = [-1, 10, -20, 2, -90, 60, 45, 20]
solution = [i*i for i in new_arr if i < 0]
negative_no = [number if number >
               0 else 'negative number' for number in new_arr]
print(solution)
print(negative_no)

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     print(arr[i])
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ")


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
print(fruit_list2)
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print(fruit_list1)
print(fruit_list2)
print(fruit_list3)

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

# print(sum)

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
# print(fun(data[0]))

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
# print(t, v[0])

a=[1,2,3,4,5]
# print(a[3:0:-1])
# print(a[2:0:-2])
print(a[::2])

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())
    
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)
