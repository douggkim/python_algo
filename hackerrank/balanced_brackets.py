# What I learned 
# 1) remember to include length check conditions 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    flag = 'YES'
    stack = []
    for _ in s: 
        if _ == '{' or _=='[' or _=='(': 
            stack.append(_)
        else: 
            if len(stack) == 0: 
                   flag = 'NO'
                   return flag 
            if _ == '}': 
                if stack[-1] == '{' : 
                    stack.pop()
                else: 
                    flag = 'NO'
                    return flag 
            elif _ == ']':
                if stack[-1] == '[' :
                    stack.pop()
                    pass  
                else: 
                    flag = 'NO'
                    return flag 
            elif _ == ')':
                if stack[-1] == '(':
                    stack.pop()
                else: 
                    flag = 'NO'
                    return flag 
    if len(stack)!=0: 
        flag = 'NO'
        return flag
    return flag
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
