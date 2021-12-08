# trapping rain water
'''
The idea is to traverse every array element and find the highest bars on the left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element.
'''

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
    
solve([ 3,0,4,2,3])