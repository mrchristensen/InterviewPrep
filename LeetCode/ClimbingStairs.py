# https://leetcode.com/problems/climbing-stairs/
# Runtime: 29 ms, faster than 95.46% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 96.23% of Python3 online submissions for Climbing Stairs.

# 18 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        num_prev = 1
        num_prev_prev = 1
        num = 1
        
        for i in range(2,n+1):
            num = num_prev + num_prev_prev
            num_prev_prev = num_prev
            num_prev = num
        
        return num
