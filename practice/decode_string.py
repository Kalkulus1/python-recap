"""
Initialize an empty stack to keep track of the characters and their counts.
Iterate through each character in the input string.
If the character is a digit, we need to handle the case of multiple digits. Keep track of the current number by continuously multiplying it by 10 and adding the new digit. For example, if we have "32[a]", we start with 3, then encounter 2, so the current number becomes 3 * 10 + 2 = 32.
If the character is an opening bracket '[', we push the current number and an empty string to the stack. The current number represents the count of the characters to be repeated, and the empty string will store the decoded substring.
If the character is a closing bracket ']', we pop the top of the stack to get the count and substring. Repeat the substring count times and append it to the decoded string stored in the stack below. If there is a string already present in the stack below the current level, append the newly repeated substring to it.
If the character is a letter, we simply append it to the current level's substring in the stack.
After iterating through all the characters in the input string, the stack will contain the decoded string.
"""

def decodeString(s):
    stack = []  # Stack to store the numbers and partial decoded strings
    curr_num = 0  # Current number to track the count of characters to be repeated
    curr_str = ''  # Current partial decoded string

    for char in s:
        if char.isdigit():  # If the character is a digit, update the current number
            curr_num = curr_num * 10 + int(char)
        elif char == '[':  # If the character is an opening bracket, push the current number and partial string to the stack
            stack.append((curr_num, curr_str))
            curr_num = 0  # Reset the current number for the next repetition
            curr_str = ''  # Reset the current partial string for the next repetition
        elif char == ']':  # If the character is a closing bracket, pop from the stack to repeat the string
            count, prev_str = stack.pop()  # Get the previous count and partial string from the stack
            curr_str = prev_str + count * curr_str  # Repeat the current string count times and append it to the previous string
        else:  # If the character is a letter, append it to the current string
            curr_str += char

    return curr_str

# Example test cases
s1 = "3[a]2[bc]"
print(decodeString(s1))  # Output: "aaabcbc"

s2 = "3[a2[c]]"
print(decodeString(s2))  # Output: "accaccacc"
