# What I learned 
# 1) if you want to change a part of string 
# alp = alp[:i]+target+alp[i+1:]
# 2) ord({letter}): return the ascii code 
# 3) chr({number}): return the character corresponding to the ascii code 
# 4)ASCII 
# uppercase: 65~90 
# lowercase: 97~122 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    k%=26
    tot = len(s)
    for i in range(tot):
        asc = ord(s[i])
        if asc<65 or (90<asc and asc<97) or 122<asc: 
            continue 
        elif 65<= asc and asc<=90: 
            if 65<=asc+k and asc+k<=90: 
                s=plus_3(s,i,k)
            else: 
                s=plus_3_return(s,i,65,90,k)
        elif 97<= asc and asc<=122: 
            if 97<=asc+k and asc+k<=122: 
                s=plus_3(s,i,k)        
            else: 
                s=plus_3_return(s,i,97,122,k)
            
    
    
    return s

def plus_3(alp,i,k):
    target = ord(alp[i][0])
    target+=k
    target = chr(target)
    alp = alp[:i]+target+alp[i+1:]
    
    return alp

def plus_3_return(alp,i,lowr,highr,k):
    target = ord(alp[i][0])
    target= (target+k)%highr +(lowr-1)
    target = chr(target)
    alp = alp[:i]+target+alp[i+1:]
    
    return alp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
