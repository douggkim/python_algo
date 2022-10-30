# What I learned 
# 1) use heapq to use ordered list for problems 
# 2) heapq.heapify({list}) - > don't assign to variable 
# 3) heapq.heappop() -> pop the smallest value 
# 4) heapq.heappush({element}) -> add to heap 
# 5) A[0] -> smallest element

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    cnt = 0 
    heapq.heapify(A)
    if A[0]>=k: 
        return cnt 
    
    while len(A)>=2: 
        l = heapq.heappop(A)
        l2 = heapq.heappop(A)
        heapq.heappush(A,l2*2+l)
        cnt+=1
        if A[0]>=k:
            return cnt 

    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
