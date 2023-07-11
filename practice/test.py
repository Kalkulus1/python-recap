

def decode_string(s: str):
    stack = []
    curr_num = 0
    curr_str = ''


    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        
        elif char == "[":
            stack.append((curr_num, curr_str))
            curr_num = 0
            curr_str = ''
        
        elif char == "]":
            count, prev_str = stack.pop()
            print(count, prev_str)
            curr_str = prev_str + count * curr_str
            print(curr_str)
        
        else:
            curr_str += char
    
    return curr_str

# # Example test cases
# s1 = "3[a]2[bc]"
# print(decode_string(s1))  # Output: "aaabcbc"

s2 = "3[a2[c]]"
print(decode_string(s2))  # Output: "accaccacc"
