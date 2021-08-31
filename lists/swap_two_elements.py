def swap(l, p1, p2):
    l[p1], l[p2] = l[p2], l[p1]
    return l

print(swap([12, 35, 9, 56, 24], 1, 4))