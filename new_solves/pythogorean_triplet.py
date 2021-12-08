from itertools import combinations
def pythagorean_triplet(array):
    squared_num = dict((num**2, num) for num in array)
    triplet = [(squared_num[x], squared_num[y], squared_num[x+y])
                for x, y in combinations((squared_num), 2) if x+y in squared_num.keys()]
    return triplet

print(pythagorean_triplet([1,2,3,4,5,6,7,8]))



# Python program to check if there exists a pythagorean triplet
def checkTriplet(arr, n):
	for i in range(n):
		arr[i] = arr[i] * arr[i]

	arr.sort()

	for i in range(n - 1, 1, -1):
		s = set()
		for j in range(i - 1, -1, -1):
			if (arr[i] - arr[j]) in s:
				return True
			s.add(arr[j])
	return False

# Driver Program
arr = [3, 2, 4, 6, 5]
n = len(arr)
if (checkTriplet(arr, n)):
	print("Yes")
else:
	print("No")

# This is contributed by Manvi Pandey
