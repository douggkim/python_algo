#  Things to think about 
# 1) What if the array len == 0?  you can't .pop() or do array[-1]


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for i in s: 
            if i =="(" or i=="[" or i=='{': 
                stack.append(i)
            elif i==")":
                if not stack or stack.pop() != "(": 
                    return False
            elif i=="]": 
                if not stack or stack.pop() != "[": 
                    return False
            elif i=="}": 
                if not stack or stack.pop() != "{": 
                    return False 
        
        return not stack
                