def search(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        print(mid)
        print(array[mid])
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(search([-2,3,4,7,8,9,11,13], 11))

def find_target_index(array, target):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2

        if array[mid_index] == target:
            return mid_index
        elif target < array[mid_index]:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    
    return -1
print(find_target_index([-2,3,4,7,8,9,11,13], 11))