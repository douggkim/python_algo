# What I need to think about 
# 1) think about out of index errors 
# 2) think about which way we'll move next (only sideways)


# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # define m,n, cnt 
        m = len(grid)
        n = len(grid[0])
        cnt = 0 
        # define check matrix 
        check = [["0" for i in range(n)] for i in range(m)]

        # define traverse function 
        def traverse(i:int,j:int,check:List[List[str]], grid:List[List[str]]) -> List[List[str]]: 
            check[i][j]='1'
            ver_list = [i-1,i+1]
            hor_list = [j-1,j+1]
            for ver in ver_list: 
                if ver>= 0 and ver <m and check[ver][j]!= '1' and grid[ver][j]!='0': 
                    check = traverse(ver,j,check,grid)
            for hor in hor_list: 
                if hor>=0 and hor <n and check[i][hor] != '1' and grid[i][hor]!='0':
                    check = traverse(i,hor,check,grid)
            

            return check

        # run the function when check != 1 
        for i in range(m):
            for j in range(n): 
                if check[i][j] != '1' and grid[i][j] != '0': 
                    
                    cnt += 1 
                    check = traverse(i,j,check,grid)
                    
        
        return cnt
                    