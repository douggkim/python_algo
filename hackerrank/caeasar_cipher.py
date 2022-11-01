# # What I learned 
# # 1) if you want to change a part of string 
# # alp = alp[:i]+target+alp[i+1:]
# # 2) ord({letter}): return the ascii code 
# # 3) chr({number}): return the character corresponding to the ascii code 
# # 4)ASCII 
# # uppercase: 65~90 
# # lowercase: 97~122 
# 5) you could use string  'abcdefghijklmnopqrstuvwxyz'
# 6) check upper with isupper() 
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
    alph = 'abcdefghijklmnopqrstuvwxyz'
    result_str = ''
    new_alph = {}
    
    for i in range(len(alph)): 
        new_alph[alph[i]] = alph[(i+k)%len(alph)]
        
    for i in range(len(s)): 
        if s[i].lower() in new_alph.keys(): 
            if s[i].isupper(): 
                result_str += new_alph[s[i].lower()].upper()
            else : 
                result_str += new_alph[s[i].lower()]
        else: 
            result_str+=s[i]
                
                
    return result_str
            
    
    
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
