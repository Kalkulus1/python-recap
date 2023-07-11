# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
  stack = []
  for i in myStr:
    if i in open_list:
      stack.append(i)
      
    elif i in close_list:
      pos = close_list.index(i)
      if ((len(stack) > 0) and
        (open_list[pos] == stack[len(stack)-1])):
        stack.pop()
        
      else:
        return "Unbalanced"
  if len(stack) == 0:
    return "Balanced"
  return "Unbalanced"
# Driver code
string = "{[]{()}}"
# print(string,"-", check(string))

# string = "[{}{})(]"
# print(string,"-", check(string))

# string = "((()"
# print(string,"-",check(string))






def getBrackets(s):
    
    cnt = 0

    for i in s:

        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt<0: 
            print("Not Balanced!...")
            break
            
    if cnt == 0:
        print('Balanced!')
    else:
        print('Not Balanced!')
        

getBrackets('()(())')




def getParenethesis(string):
    open_p = ["[", "(", "{"]
    close_p = ["]", ")", "}"]
    
    stack = []
    
    for elmnt in string:
        if elmnt in open_p:
            stack.append(elmnt)
        elif elmnt in close_p:
            pos = close_p.index(elmnt)
            if ((len(stack) > 0) and
                (open_p[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    
    if len(stack) == 0:
        return "Balanced"
    return "Unbalanced"
        
print(getParenethesis("()"))    
string = "[((()))][]{}"
print(string,"-",getParenethesis(string))