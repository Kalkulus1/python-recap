def search(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(search([-2,3,4,7,8,9,11,13], 11))