from itertools import combinations


def repeatingDecimal(num, den):

    # Check if denominator is zero
    if den == 0:
        return 'NaN'

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




# Problem Name is &&& Largest Tree &&& PLEASE DO NOT REMOVE THIS LINE.
""" 
  Instructions:

  Given a forest ( one or more disconnected trees ), find the root of largest tree 
  and return its Id. If there are multiple such roots, return the smallest Id of them.

  Complete the largestTree function in the editor below.
  It has one parameter, immediateParent, which is a map containing key-value pair indicating 
  child -> parent relationship. The key is child and value is the corresponding 
  immediate parent. 
  Constraints
    - Child cannot have more than one immediate parent.
    - Parent can have more than one immediate child.
    - The given key-value pair forms a well-formed forest ( a tree of n nodes will have n-1 edges )

  Example:

  Input:
  { { 1 -> 2 }, { 3 -> 4} }   

  Expected output: 2
  Explanation: There are two trees one having root of Id 2 and another having root of Id 4.
  Both trees have size 2. The smaller number of 2 and 4 is 2. Hence the answer is 2. 
""" 


""" Find the largest tree. """
def largestTree(immediateParent):
    # TODO: implement this function
    return 0

def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """

    testCases = [
        # example
        (dict({1:2, 3:4}),
         2),
    ]

    passed = True
    for tc, expected in testCases:
        actual = largestTree(tc)
        if actual != expected:
            passed = False
            print("Failed for case ", tc, "\n  expected ", expected, ", actual ", actual)

    return passed


if name == "main":
    result = doTestsPass()

    if result:
        print("All tests pass\n");
    else:
        print("Tests fail\n");