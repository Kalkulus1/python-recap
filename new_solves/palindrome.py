# def palindrome(string):
#     new_string = string.lower()
#     print(new_string)
#     reversed_string = new_string[::-1]
#     # reversed_string = reversed(new_string)
    
#     return list(new_string) == list(reversed_string)

# print(palindrome("aIbohPhoBiA"))


x = "aIbohPhoBiA".lower()
 
w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")
    

def palindrome(string):
    new_string = string.lower()
    
    reversed_string = []
    
    for char in range(len(string)-1, -1, -1):
        
        reversed_string.append(new_string[char])
        
    return ''.join(reversed_string) == new_string

def palindrome(string):
    new_string = string.lower()
    reversed_string = new_string[::-1]   
    return reversed_string == new_string
print(palindrome("Ama"))
print(palindrome("aIbohPhoBiA"))

def sortList(array):
    
    new_array = []
    
    while array:
        
        minimum = array[0]
        
        for element in array:
            if element < minimum:
                minimum = element
                
        new_array.append(minimum)
        array.remove(minimum)
        
    return new_array
    
print(sortList([-5, -23, 5, 0, 23, -6, 23, 8, 67]))

from random import random
data = dict()
for element in range(-5, -11, -1):
   data[element] = random()

result = dict(sorted(data.items(), key=lambda item: item[1]))

print(result)

# from random import random
# import csv

# # previous code to generate data
# result = dict()
# for element in range(-5, -11, -1):
#    result[element] = random()

# header = ['keys', 'values']

# with open('data.csv', 'w', encoding='UTF8') as f:
#     # csv writer
#     writer = csv.writer(f)
#     # write header
#     writer.writerow(header)
#     # write data
#     writer.writerows(list(result.items()))