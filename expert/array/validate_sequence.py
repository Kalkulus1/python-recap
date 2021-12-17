def isValidSubsequence(array, sequence):
	position = 0
	for element in array:
		if position < len(sequence) and sequence[position] == element:
			position += 1
	return position == len(sequence)

print(isValidSubsequence([1,2,3,4,5],[2,3,5]))

def validate_subsequence(arr1,arr2):
    c=[]
    j = arr2.copy()
    for i in arr1:
        if i == arr2[0]:
            c.append(arr2[0])
            arr2.pop(0)
    return c == j

print(validate_subsequence([1,2,3,-5,3,4,5],[2,3,-5,5]))