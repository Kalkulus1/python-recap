from itertools import combinations


def repeatingDecimal(num, den):

    # Check if denominator is zero
    if den == 0:
        return 'NaN'

    # Check if numerator is zero
    if num == 0:
        return '0'

    # Check if the remainder is zero, just return the answer then
    # Check for divisibility
    if num % den == 0:
        print(str(num // den))
        return str(num // den)

    # Check for negatives
    negative = num * den < 0

    # Let's work with the absolute values since we already took care of negatives
    numerator = abs(num)
    denominator = abs(den)

    output = []
    if negative:
        output.append("-" + str(numerator // denominator))
    else:
        output.append(str(numerator // denominator))

    output.append(".")

    num_q = []
    while True:
        remainder = numerator % denominator

        # if remainder is zero, let's break after
        if remainder == 0:
            for element in num_q:
                output.append(str(element[-1]))
            break

        # Get new numerator and quotient
        numerator = remainder * 10
        quotient = numerator // denominator

        if [numerator, quotient] not in num_q:
            num_q.append([numerator, quotient])

        else:
            index = num_q.index([numerator, quotient])
            for element in num_q[:index]:
                output.append(str(element[-1]))

            output.append("(")
            for element in num_q[index:]:
                output.append(str(element[-1]))

            output.append(")")
            break
    print(''.join(output))
    return ''.join(output)


def doTestsPass():
    testPassed = True
    testPassed &= repeatingDecimal(1, 0) == "NaN"
    testPassed &= repeatingDecimal(1, 2) == "0.5"
    testPassed &= repeatingDecimal(1, 3) == "0.(3)"
    testPassed &= repeatingDecimal(1, 4) == "0.25"
    testPassed &= repeatingDecimal(2, 11) == "0.(18)"
    testPassed &= repeatingDecimal(4, 11) == "0.(36)"
    testPassed &= repeatingDecimal(5, 3) == "1.(6)"
    testPassed &= repeatingDecimal(-10, 5) == "-2"
    testPassed &= repeatingDecimal(34, 15) == "2.2(6)"
    testPassed &= repeatingDecimal(100, 26) == "3.(846153)"

    if testPassed:
        print("Tests passed")
        return 0
    print("Tests Failed")
    return 1

# doTestsPass()
# repeatingDecimal(1, 2)
# repeatingDecimal(1, 3)
# repeatingDecimal(1, 4)
# repeatingDecimal(1, 5)
# repeatingDecimal(1, 6)
# repeatingDecimal(1, 7)


def numberOfWays(N):
    count = 0
    n = 2
    while 2*N + n - n**2 > 0:
        a = (2*N + n - n**2) / (2*n)
        if a - int(a) == 0:
            print(a, n)
            count += 1
        n += 1
    return count
# print(numberOfWays(4))

def pythagorean_triplet(array):
    squared_num = dict((num**2, num) for num in array)
    triplet = [(squared_num[x], squared_num[y], squared_num[x+y])
                for x, y in combinations((squared_num), 2) if x+y in squared_num.keys()]
    return triplet

# print(pythagorean_triplet([1,2,3,4,5,6,7,8]))


# trapping rain water

def solve(A):

    left_max = []
    prev_max = 0
    for i in A:
        prev_max = max(prev_max, i)
        left_max.append(prev_max)

    prev_max = 0
    right_max = []

    for i in range(len(A)-1, -1, -1):
        prev_max = max(A[i], prev_max)
        right_max.append(prev_max)

    score = 0
    right_max.reverse()
    for idx, val in enumerate(A):
        if idx == 0 or idx == len(A)-1:
            continue

        max_to_left = left_max[idx-1]
        max_to_right = right_max[idx+1]
        min_of_both_sides = min(max_to_left, max_to_right)
        if min_of_both_sides > val:
            score += min_of_both_sides - val

    print(score)


# solve([ 3,0,4,2,3])


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


# print(c[len(c)//2] if len(c)%2==1 else (c[len(c)//2-1]+c[len(c)//2] // 2))


def isValidSubsequence(array, sequence):

    pos = 0

    for element in array:

        if pos <= len(sequence) - 1 and sequence[pos] == element:

            pos += 1

    return pos == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))


def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes
def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)
def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors

print(riverSizes([
    [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]))
