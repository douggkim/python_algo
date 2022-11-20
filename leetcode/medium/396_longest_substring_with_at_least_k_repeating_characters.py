# What I learned 
# 1) Divide and conquer 
# 2) s.count(c) 

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0 
        for c in set(s):
            if s.count(c)<k: 
                return max(self.longestSubstring(part,k) for part in s.split(c))
        return len(s)