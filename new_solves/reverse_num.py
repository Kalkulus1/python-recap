def reverse(number):
    # declare a reverse_num to zero
    reverse_num = 0
    
    # Check if the number is not zero
    while number != 0:
        
        # get the remainder
        remainder = number % 10
        
        # find the reverse number
        reverse_num = (reverse_num*10) + remainder
        
        # Get the number that is left
        number //= 10
    
    #return the final value after the loop finishes
    return reverse_num


print(reverse(1234))

def reverseNum(number):
    return str(number)[::-1]

print(reverseNum(1234))