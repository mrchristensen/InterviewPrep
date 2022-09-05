# https://leetcode.com/problems/contains-duplicate/
# Runtime: 454 ms, faster than 98.11% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 25.9 MB, less than 68.78% of Python3 online submissions for Contains Duplicate.

# 2 minutes

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False
        
    
# Runtime: 642 ms, faster than 58.68% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 28.71% of Python3 online submissions for Contains Duplicate.

# Time Complexity: O(n)
# Space Complexity: O(1)

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
        
#         previous = -10000000001
#         for num in nums:
#             if(num == previous):
#                 return True
#             previous = num
            
#         return False
