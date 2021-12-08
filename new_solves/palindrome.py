def palindrome(string):
    new_string = string.lower()
    print(new_string)
    reversed_string = new_string[::-1]
    # reversed_string = reversed(new_string)
    
    return list(new_string) == list(reversed_string)

print(palindrome("aIbohPhoBiA"))


x = "aIbohPhoBiA".lower()
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes")
else:
    print("No")