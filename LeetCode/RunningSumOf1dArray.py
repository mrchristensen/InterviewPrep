# https://leetcode.com/problems/running-sum-of-1d-array/
# Runtime: 34 ms, faster than 99.12% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.1 MB, less than 27.31% of Python3 online submissions for Running Sum of 1d Array.

# 2 minutes

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_totals = []
        total = 0
        
        for num in nums:
            total += num
            running_totals.append(total)
            
        return running_totals
