# run length encoding
'''
a) Pick the first character from the source string. 
b) Append the picked character to the destination string. 
c) Count the number of subsequent occurrences of the picked character and append the count to the destination string. 
d) Pick the next character and repeat steps b) c) and d) if the end of the string is NOT reached.
'''
def printRLE(st):

	n = len(st)
	i = 0
	while i < n- 1:

		# Count occurrences of
		# current character
		count = 1
		while (i < n - 1 and st[i] == st[i + 1]):
			count += 1
			i += 1
		i += 1

		# Print character and its count
		print(st[i - 1] + str(count), end = "")

# Driver code
if __name__ == "__main__":

	st = "wwwwaaadexxxxxxyaawww"
	printRLE(st)
