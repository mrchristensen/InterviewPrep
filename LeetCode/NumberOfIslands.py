# https://leetcode.com/problems/number-of-islands/
# Runtime: 307 ms, faster than 94.09% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.4 MB, less than 81.29% of Python3 online submissions for Number of Islands.

# 30 minutes

# Time Complexity: O(n x m)
# Space Complexity: O(1)

class Solution:
    def __init__(self):
        self.n, self.m = 0, 0
        self.visited_land = "2"
        self.unvisited_land = "1"
        self.directions = [[0,1], [0,-1], [1,0], [-1,0]]
        self.grid = None
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        islands = 0
        i, j = 0, 0
        
        # Run DFS whenever we hit new ground
        for i in range(self.n):
            for j in range(self.m):
                if(self.grid[i][j] == self.unvisited_land):
                    islands += 1
                    self.dfs(i, j)

        return islands
    
    
    def dfs(self, i, j):
        self.grid[i][j] = self.visited_land
        
        # For each neighbour
        for delta in self.directions:
            new_i = i + delta[0]
            new_j = j + delta[1]
            
            # If valid move
            if(0 <= new_i < self.n and 0 <= new_j < self.m):
                # And unvisted land
                if(self.grid[new_i][new_j] == self.unvisited_land):
                    self.dfs(new_i, new_j)
        
