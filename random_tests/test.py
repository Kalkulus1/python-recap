def convert(s):

    alist = []

    alist[:0] = s

    # blist = []
    # for i in s:
    #     blist.append(i)
    # print(blist)

    print(''.join(reversed(alist)))

    print(s[::-1])

convert('1122345678')


def getBrackets(s):
    
    cnt = 0

    for i in s:

        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt<0:
            print("Not Balanced!")
            break
            
    else:
        print('Balanced!')

getBrackets('((()))')



total = [0]
count = [0]
def nestedList(l):

    for i in l:
        
        if type(i) == int:

            total[0] += i
            count[0] += 1

        else:
            nestedList(i)

nestedList([1,2,[3,3,[4],5],4,6,1,1])
print(f'The total is {total[0]}')
print(f'Average is: {total[0]/count[0]}')

def returnList(lst, num):
    alist = []

    for i in lst:
        if i != num:
            alist.append(i)
    
    return alist

print(returnList([1,2,3,5,5,5,6,4,6,6], 5))
    
from collections import Counter
def extractElements(lst, K):

    dct = dict(Counter(lst))
    # dct = {}

    # for i in lst:
    #     if i in dct:
    #         dct[i] += 1
    #     else:
    #         dct[i] = 1
    
    alist = []

    for i,j in dct.items():

        if j > K:
            alist.append(i)

    return alist
print(extractElements([4,6,4,3,3,4,3,4,3,8], 3))
print(extractElements([4,6,4,3,3,4,3,4,6,6], 2))


def consOccur(lst):

    for i in range(len(lst) -2):

        if lst[i] == lst[i+1] and lst[i+1] == lst[i+2]:

            print(lst[i])

consOccur([4,5,5,5,3,8,22,22,22])


from itertools import permutations, combinations

# a = [1,2,3,4]

# p = list(permutations(a))
# c = list(combinations(a, 3))
# print(c)

def maxOfNumbers(lst):

    numbers = list(permutations(lst))

    numStr = []
    for group in numbers:

        numStr.append(''.join([str(x) for x in group]))
    
    # numStripped = [x.lstrip('0') for x in numStr]

    numbers = [int(x) for x in numStr]

    print(max(numbers))

maxOfNumbers([1,34,3,98,9,76,45,4])


def newMaxOfNumbers(lst):

    numbers = list(permutations(lst))

    numStr = []

    for group in numbers:
        numStr.append(''.join([str(x) for x in group]))
    
    numbers = [int(x) for x in numStr]
    print(max(numbers))

newMaxOfNumbers([1,34,3,98,9,76,45,4])