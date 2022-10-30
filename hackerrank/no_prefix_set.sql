-- What I learned
-- 1) use "Trie" for letter based graphs 
-- 2) you can use dict for "Trie"
-- 3) when you assign python dict as variables, it's not going to renew the dict. 
--    It will only point to the existing graph



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    
    trie = {} 
    
    for word in words: 
        curr = trie 
        
        for i in range(len(word)):
            letter = word[i]
            
            if letter in curr: 
                curr = curr[letter]
                
                if not curr : 
                    print("BAD SET")
                    print(word)
                    return 
                
                if len(word)-1 == i : 
                    print("BAD SET")
                    print(word)
                    return 
            else: 
                curr[letter]={}
                curr = curr[letter]
    print("GOOD SET")
                    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
