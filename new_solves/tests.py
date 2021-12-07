def countNumDigits(number):
    
    if number < 0:
        number_str = str(number)
        result = number_str.replace('-', '')
        return len(result)
    
    return len(str(number))


# print(countNumDigits(10111))


def countNumDigitss(number):
    
    count = 0
    
    while number != 0:
        number //= 10
        
        count += 1
        
    return count

# print(countNumDigitss(10111))


def palindrome(string):
    new_string = string.casefold()
    
    reversed_string = new_string[::-1]
    reversed_string = reversed(new_string)
    
    return list(new_string) == list(reversed_string)

# print(palindrome("aIbohPhoBiA"))

def armstrongNumber(number):
    order = len(str(number))
    total = 0
    
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
      
    if number == total:
        return f"{number} is an Armstrong number"
    else:
        return f"{number} is not an Armstrong number"

# print(armstrongNumber(407))
# print(armstrongNumber(153))


def armstrongNumberRange(lower, upper):
    
    # Get all the numbers
    for number in range(lower, upper + 1):
        
        # get order or degree
        order = len(str(number))
        
        # initialize total value
        total = 0

        # Get all digits and calculate the total
        temp = number
        while temp > 0:
            digit = temp % 10
            total += digit ** order
            temp //= 10
        
        # check the total and number and print the number is an Armstrong number
        if number == total:
            print(number)

# print(armstrongNumberRange(100, 2000))



def swap(l, p1, p2):
    l[p1], l[p2] = l[p2], l[p1]
    return l

# print(swap([12, 35, 9, 56, 24], 1, 4))


def getAnswer(num, den, msg):
    '''
    Returns the result of dividing two numbers
    '''
    try:
        return num/den
    except ZeroDivisionError:
        return msg

# print(getAnswer(3, 0, "Error Division"))



# Find the first non-repeating character in a string

# Example
## Input: kubyk
## Output: u

## Input: kubuyk
## Output: b

def firstNonRepeatElement(string):
    
    # declare an empty dict
    count = {}
    
    # get the letter
    for letter in string:
        
        # Check if letter exists
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    # get elements in the final list
    for k in count:
        if count[k] == 1:
            print(k)
            break
        
# firstNonRepeatElement("kubybku")

from collections import Counter

def firstLetter(letters):

    dct = dict(Counter(letters))

    print(dct)

    for letter in dct:

        if dct[letter] == 1:

            print(letter)

            break

# firstLetter('kubyk')
# firstLetter('kubuyk')


# Get consonants in a sentence

def getConsonants(sentence):
    '''
    Returns consonants in a sentence
    '''
    # Since the vowels are not much, I can declare them in a set
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    result = []
    
    for letter in sentence:
        
        if letter not in vowels:
            
            result.append(letter)
    
    return ''.join(result)
    
# print(getConsonants('I am going to school'))


def convert(s):
    
    alist = []

    alist[:0] = s

    # blist = []
    # for i in s:
    #     blist.append(i)
    # print(blist)
    
    print(alist[:1])

    print(''.join(reversed(list(s))))

    print(s[::-1])

# convert('1122345678')


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

# getBrackets('((()))')



# Declare variables
total = [0]
count = [0]

def nestedList(l):

    for i in l:
        
        if type(i) == int:
            total[0] += i
            count[0] += 1

        else:
            nestedList(i)

    return f'The total is {total[0]}. Average is: {total[0]/count[0]}'

# print(nestedList([1,2,[3,3,[4],5],4,6,1,1]))

# Another approach
def averageNestedList(arr):
    new = list(str(arr))
    b = []
    
    for s in new:
        if s.isnumeric():
            b.append(int(s))
            
    c = sum(b)
    average = sum(b)/len(b)
    return [c,average]

# print(averageNestedList([1,2,[3,3,[4],5],4,6,1,1]))

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

# print(extractElements([4,6,4,3,3,4,3,4,3,8], 3))
# print(extractElements([4,6,4,3,3,4,3,4,6,6], 2))

def consOccur(lst):
    result = set()
    for i in range(len(lst) - 2):
        if lst[i] == lst[i+1] and lst[i+1] == lst[i+2]:
            result.add(lst[i])
    return result
# print(consOccur([4,4,5,5,5,3,8,22,22,22]))

def pairSum(num1, num2):
    return num1+num2
def pairSumSequence(num):
    result = 0
    for i in range(num):
        result += pairSum(i, i+1)
    return result
# print(pairSumSequence(3))

def getUniquePairs(aset, k):
    result = 0
    ans = []
    for i in aset:
        if i+k in aset:
            result += 1
            ans.append((i,i+k))
    return result, ans

print(getUniquePairs({1,7,5,9,2,12,3}, 2))

    
    