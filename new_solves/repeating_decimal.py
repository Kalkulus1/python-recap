
def repeatingDecimal(num, den):
    # check if it's NaN
    if den == 0:
        return "NaN"
    
    # check if it's divisible completely
    if num % den == 0:
        return f"{num//den}"
    
    # check for negative
    negative = num * den < 0

    numerator = abs(num)
    denominator = abs(den)

    output = []
    if negative:
        output.append(f"-{numerator // denominator}")
    else:
        output.append(f"{numerator // denominator}")
    output.append(".")
    num_q = []
    while True:
        remainder = numerator % denominator

        if remainder == 0:
            for element in num_q:
                output.append(f"{element[-1]}")
            break

        numerator = remainder * 10
        quotient = numerator // denominator

        if [numerator, quotient] not in num_q:
            num_q.append([numerator, quotient])
        
        else:
            index = num_q.index([numerator, quotient])

            for element in num_q[:index]:
                output.append(f"{element[-1]}")

            output.append("(")

            for element in num_q[index:]:
                print(num_q[index:])
                output.append(f"{element[-1]}")
            
            output.append(")")

            break

    print("".join(output))
    return "".join(output)


def doTestsPass():
    testPassed = True
    testPassed &= repeatingDecimal(1, 0) == "NaN"
    testPassed &= repeatingDecimal(4, 2) == "2"
    testPassed &= repeatingDecimal(1, 2) == "0.5"
    testPassed &= repeatingDecimal(1, 3) == "0.(3)"
    testPassed &= repeatingDecimal(1, 4) == "0.25"
    testPassed &= repeatingDecimal(2, 11) == "0.(18)"
    testPassed &= repeatingDecimal(4, 11) == "0.(36)"
    testPassed &= repeatingDecimal(5, 3) == "1.(6)"
    testPassed &= repeatingDecimal(-10, 5) == "-2"
    testPassed &= repeatingDecimal(34, 15) == "2.2(6)"
    testPassed &= repeatingDecimal(100, 26) == "3.(846153)"

    if testPassed:
        print("Tests passed")
        return 0
    print("Tests Failed")
    return 1

doTestsPass()
# print(repeatingDecimal(-4, 2))
# print(repeatingDecimal(4, 2))
# print(repeatingDecimal(1, 2))
# print(repeatingDecimal(1, 3))
# repeatingDecimal(1, 4)
# repeatingDecimal(1, 5)
# repeatingDecimal(1, 6)
# repeatingDecimal(1, 7)