# what is permutation -> same words, but in different order
# eg -> peek -> keep, rail -> lair

def perumtation(list1, list2):
    if len(list1) != len(list2):
        return 'Cannot be permutation cause they are not the same length'
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


print(perumtation([1, 3, 2], [3, 1, 2]))


def perumtation_for_string(string1, string2):
    if len(string1) != len(string2):
        return 'Cannot be permutation cause they are not the same length'
    arr1 = string1.split()
    print(arr1)
    arr2 = string2.split()
    print(arr2)
    sorted1 = ''.join(sorted(arr1[0]))
    sorted2 = ''.join(sorted(arr2[0]))
    if sorted1 == sorted2:
        return True
    # arr1.join()
    # arr2.join()
    return False


print(perumtation_for_string('feranmi', 'asferto'))
