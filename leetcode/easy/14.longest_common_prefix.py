# What I learned
# 1) Be ware of the conditions 
# 2) look at the data range before solving the problem

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # EC 1 : len 1 -> return 
        if len(strs) == 1:
            return strs[0]
        # Get the smallest length 
        min = 201
        for st in strs: 
            if len(st) < min: 
                min = len(st)
        # Loop through letters 
        if min == 0: 
            return ""
        result = ""
        for i in range(min):
            for j in range(len(strs)): 
                
                if j == 0 : 
                    target = strs[j][i] 
                    print(target)
                
                elif j == len(strs)-1: 
                    if strs[j][i] == target: 
                        result = result+target
                        
                    else: 
                        return result 
                
                else: 
                    if strs[j][i] != target: 
                        return result
                
                        
        
        
        return result
                        
                        
                    
                    
                
        # loop through list 
        # if first save letter 
        # others  check if same 
        # if last and same add the letter 
        