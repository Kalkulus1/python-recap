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