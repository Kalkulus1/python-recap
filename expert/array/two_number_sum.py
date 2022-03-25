def twoNumberSum(array, targetSum):
    result = []
    for num in array:
        for i in array:
            if num != i and num + i == targetSum and num not in result and num not in result:
                result = [num, i]

    return result


def twoNumberSum(array, targetSum):
    result = []
    for num in array:
        if num not in result and targetSum - num in array:
            result = [num, targetSum - num]

    return result


def twoNumberSum(array, targetSum):
    numbers = {}
    for num in array:
        match = targetSum - num
        if match in numbers:
            return [match, num]
        else:
            numbers[num] = True
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
