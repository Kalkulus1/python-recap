def getUniquePairs(aset, k):
    result = 0
    ans = []
    for i in aset:
        if i+k in aset:
            result += 1
            ans.append((i,i+k))
    return result, ans

# print(getUniquePairs({1,7,5,9,2,12,3}, 2))