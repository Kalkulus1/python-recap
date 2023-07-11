x = [1, 2, 3, 4, 5, 6, 8, 14]

mp = map(lambda i: i * i, x)

print(list(mp))

f = filter(lambda i: i % 2 == 0, x)
print(list(f))
