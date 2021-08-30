
from itertools import combinations
def pair_sum(lst, k):

    if len(lst) < 2:
        print('Array is too small')
        
    numbers = list(combinations(lst, 2))
    print(numbers)

    for group in numbers:
        if sum(group) == k:

            print(group)

# pair_sum([1,3,2,2,5], 6)

def pair_sum2(array, k):
    
    if len(array) < 2:
        print('Array is too small')
    
    seen = set()
    output = set()

    for num in array:

        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    for i in list(output):
        print(i)

pair_sum2([1,3,2,2], 4)




def largest_sum(array):

    if len(array) == 0:
        return print('array too small')

    max_sum = array[0]
    current_sum = array[0]

    for num in array[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    
    return max_sum


# print(largest_sum([7,1,2,-1,3,4,10,-12,3,21,-19]))



def reverse_string(string):

    l = string.split(' ')

    alist = reversed(l)

    print(' '.join(alist))

    


# reverse_string('This is the best')

def rotation(l1, l2):

    if len(l1) != len(l2):
        return False

    key = l1[0]
    key_index = 0

    for i in range(len(l2)):
        if l2[i] == key:
            key_index = i
    
            break

    if key_index == 0:
        return False

    for x in range(len(l1)):
        l2index = (key_index + x) % len(l1)

        if l1[x] != l2[l2index]:
            return False

    return True
            
# print(rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))

def commonElements(l1, l2):

    alist = []

    for i in l1:
        for j in l2:
            if i == j:
                alist.append(i)
    
    return alist

print(commonElements([1,3,4,6,7,9], [1,2,4,5,9,10]))
            