# What I learned 
# 1) when popping from the list, 
# Save the list length as number


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1, 0, -1): 
            if nums[i]==nums[i-1]: 
                nums.pop(i)
        
        return len(nums)