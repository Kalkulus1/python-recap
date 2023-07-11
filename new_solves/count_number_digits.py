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

print(countNumDigitss(10111))

def count_num_digits(num):
    num_str = str(num)

    if "-" in num_str:
        num_str = num_str.replace('-', '')
    
    return len(num_str)

print(count_num_digits(10111))
print(count_num_digits(-10111))