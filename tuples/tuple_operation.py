# + operator to add two tuples together
# * to repeat occurence of individual elements in a tuple

tupel1 = ('a', 'b', 'c', 'd', 'e')
tupel2 = ('f', 'g', 'h', 'i', 'j')

# print(tupel1 + tupel2)
# print(tupel1 * 4)

# in operator -> returns true or false
# count method
# index method
# len function
# max number
# min number
init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
# print(result)

def sum_product(input_tuple):
    # result = 1
    # for i in input_tuple:
    #     result *= i
    #     print(result)
    return sum(input_tuple), result
    
# print(sum_product((1,2,3,4)))

def element_wise_sum(tuple1, tuple2):
    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i] + tuple2[i])
    return tuple(result)

print(element_wise_sum((1,2,3,), (4,5,6))) 

# def element_wise_sum1(tuple1, tuple2):
#     for i in range(len(tuple1)):
#         return tuple(tuple1[i] + tuple2[i])

# print(element_wise_sum1((1,2,3,), (4,5,6))) 


def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))


def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]

result = [{a:b} for a,b in zip(arr1, arr2)]
print(result)

def insert_value_front(input_tuple, value_to_insert):
    new = (value_to_insert,) + input_tuple
    return new

print(insert_value_front((1,2,3),4))

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

print(concatenate_strings(('Hello', 'World', 'from', 'Python')))


def common_elements(tuple1, tuple2):
    res = []
    for i in range(len(tuple1)):
        if tuple1[i] in tuple2:
            res.append(tuple1[i])
    return tuple(res)
    
print(common_elements((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))

def common_elements1(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

