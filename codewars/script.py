def reverse_words(text):
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    output = " ".join(reversed_words)
    return output

# print(reverse_words("This is an example"))


def reverse_words1(str):
    return ' '.join(s[::-1] for s in str.split(' '))

# print(reverse_words1("This is an example"))

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


def find_it(seq):
    # odd_number = 
    # for i in seq:
    #     if seq.count(i) % 2 != 0:
    #         return i
    #     else:
    #         return 'Not found'
    for i in seq:
        if seq.count(i)%2!=0:
            return i

print(find_it([7,1,2,3,1,5,1]))

def find_it1(seq):
    result = 0
    for num in seq:
        result ^= num
    return result

# print(find_it1([1,1,2,1]))
