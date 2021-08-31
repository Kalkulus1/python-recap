# Given a list, write a Python program to swap first and last element of the list.

## EXAMPLES

#Input : [1, 2, 3]
#Output : [3, 2, 1]

#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]

# Crazy approach
def swap(l):
    a = []

    a.append(l.pop())

    for i in l[1:]:
        a.append(i)

    a.append(l[0])
    return a

print(swap([12, 35, 9, 56, 24]))
print(swap([1, 2, 3]))

# Easiers approach
def swap2(l):
    start, *middle, end = l
    l = [end, *middle, start]
    return l

print(swap2([12, 35, 9, 56, 24]))
print(swap2([1, 2, 3]))

def swap3(l):
    temp = l[0]
    l[0] = l[len(l) - 1]
    l[len(l) - 1] = temp

    return l

print(swap3([12, 35, 9, 56, 24]))
print(swap3([1, 2, 3]))

def swap4(l):
    l[0], l[-1] = l[-1], l[0]
    return l

print(swap4([12, 35, 9, 56, 24]))
print(swap4([1, 2, 3]))

