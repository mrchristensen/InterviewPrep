# https://leetcode.com/problems/find-pivot-index/
# Runtime: 155 ms, faster than 95.25% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.1 MB, less than 92.49% of Python3 online submissions for Find Pivot Index.

# 1 hour

# Time Complexity: O(2n) = O(n)
# Space Complexity: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i, left_sum = 0, 0
        total_sum = sum(nums)
        length = len(nums)

        while(i < length):
            current_num = nums[i]
            if(left_sum == total_sum - left_sum - current_num):
                return i
            left_sum += current_num
            i += 1                
        
        return -1
