# https://leetcode.com/problems/pascals-triangle/
# Runtime: 42 ms, faster than 67.50% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 17.81% of Python3 online submissions for Pascal's Triangle.

# 30 minutes

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_index in range(1, numRows + 1):
            row = []
            for entry_index in range(row_index):
                if(entry_index == 0 or entry_index == row_index - 1):
                    row.append(1)
                else:
                    row.append(triangle[row_index - 2][entry_index-1] + triangle[row_index - 2][entry_index])
            triangle.append(row)
        
        return triangle
