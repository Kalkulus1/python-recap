def getNum(num1, num2, s):

    try:
        print(num1/num2)
    except ZeroDivisionError:
        print(s)

getNum(3, 4, 'Error Devision')