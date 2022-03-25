def consecutive(num):
    count = 0
    n = 2
    while 2*num + n - n**2 > 0:
        a = (2*num + n - n**2) / (2*n)
        if a - int(a) == 0:
            count += 1
        n += 1
    return count

print(consecutive(15))