# https://leetcode.com/problems/max-area-of-island/
# Runtime: 141 ms, faster than 92.99% of Python3 online submissions for Max Area of Island.
# Memory Usage: 16.5 MB, less than 59.41% of Python3 online submissions for Max Area of Island.

# 20 minutes

# Time Complexity: O(n x m)
# Space Complexity: O(n x m)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.directions = [[1,0], [-1,0], [0,1], [0,-1]]
        self.grid = grid
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        self.max_size = 0
        
        for i in range(self.max_i):
            for j in range(self.max_j):
                if(self.grid[i][j] == 1):
                    self.size = 0
                    self.dfs(i, j)
                    self.max_size = max(self.max_size, self.size)   
        
        return self.max_size
        
        
    def dfs(self, i, j):        
        self.size += 1
        self.grid[i][j] = 2
        
        for delta in self.directions:
            new_i, new_j = i+delta[0], j+delta[1]
            # If valid move
            if(0 <= new_i < self.max_i and 0 <= new_j < self.max_j):
                # If unvisited
                if(self.grid[new_i][new_j] == 1):
                    self.dfs(new_i, new_j)
