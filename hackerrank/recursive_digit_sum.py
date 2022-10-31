#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    n = n.strip()
    first_super=0
    for i in n: 
        first_super += int( i)
        
    first_super*=k

    first_str = str(first_super)
    while len(first_str)!=1: 
        new_super=0
        for i in first_str: 
            new_super += int(i)
        first_str=str(new_super)

        

    return first_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
