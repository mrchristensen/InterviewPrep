# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Runtime: 90 ms, faster than 94.71% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.5 MB, less than 96.42% of Python3 online submissions for Remove Duplicates from Sorted Array.

# 20 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        i = 1
        offset = 0

        while i < len(nums):
            if nums[i] == prev:
                offset += 1
            else:
                nums[i - offset] = nums[i]
                prev = nums[i]
            i += 1

        return len(nums) - offset
