'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

'''
Approach:

Initialize a Stack stack = []
Loop through the string:

    - if the current element we are traversing is the opening bracket save its corresponding closing bracket to stack
    - if the current element we are traversing is the closing bracket:
       Check Invalid cases:
        - Check if the stack is empty; if it is return False because it could be that the string could be of type s = ']' (Invalid ones)
        - Check if the top of the stack is != to the current closing element we traverse; return False (s = '[)')
       Check Valid cases:
        if stack top == current closing we are checking is same we know it is a valid one or a balanced one so far and we pop
        stack.top would be stack[-1] in case of python.
        stack.pop()


At the end if we come out of the loop we know all comparisons were valid so we return and check if stack is empty - Note we cannot return True 
directly because it is possible that we only get opening bracket as an input eg. s = '[' In this we do save corresponding closing 
bracket in the stack but that's till invalid so that's why we check stack.empty() if its empty then only we can say it is True or valid else False

Note: if we get closing bracket at start itself we return False and not traverse ahead
'''

# TC: O(n) SC: O(1)

def isValidParanthesis(str):
    stack = []

    for i in range(len(str)):
        # Opening ones
        if str[i] == '(':
            stack.append(')')
        elif str[i] == '{':
            stack.append('}')
        elif str[i] == '[':
            stack.append(']')
        # Closing ones
        elif len(stack) == 0 or stack[-1] != str[i]: # Invalid checks: We did not find same closing tags or either stack is empty since may be we got clsoing brackets at start of string
            return False
        else:
            stack.pop() # Valid ones we traverse closing brackets and found same closing in the stack top too

    return len(stack) == 0 # Cannot return True directly because it is possible that we only get opening bracket as an input eg. s = '[' In this we do save corresponding closing 
    # bracket in the stack but that's till invalid so that's why we check stack.empty() if its empty then only we can say it is True or valid else False

s = "()"
print(isValidParanthesis(s))

s = "()[]{}"
print(isValidParanthesis(s))

s = "(]"
print(isValidParanthesis(s))

s = "["
print(isValidParanthesis(s))