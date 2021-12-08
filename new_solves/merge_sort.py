a = [4, 7, 9, 9, 10, 20, 24, 25]
b = [1, 2, 3, 6, 7, 8, 9, 10, 15]

i = 0
j = 0
c = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c[len(c)//2] if len(c)%2==1 else (c[len(c)//2-1]+c[len(c)//2] // 2))