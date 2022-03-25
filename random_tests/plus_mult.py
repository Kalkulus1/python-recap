def plusMult(A):
    
    r_even = 0
    
    r_odd = 0
    
    arr_len = len(A)
    
    for i in range(0, arr_len, 4):
        r_even = (r_even + A[i])
        if i + 2 < arr_len:
            r_even = r_even * A[i+2]
    
    for i in range(1, arr_len, 4):
        r_odd = (r_odd + A[i])
        if i + 2 < arr_len:
            r_odd = r_odd * A[i+2]
    
    r_even = r_even % 2
    r_odd = r_odd % 2
    
    if r_odd > r_even:
        return "ODD"
    
    elif r_even > r_odd:
        return "EVEN"
    
    else:
        return "NEUTRAL"
    
print(plusMult([12,3,5,7,13,12]))

