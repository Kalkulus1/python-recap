def getConsonants(s1):
    
    b = {'a', 'e', 'i', 'o', 'u'}

    alist = []

    for i in s1:
        if i not in b:
            alist.append(i)

    print(''.join(alist))

getConsonants('I am going to school')