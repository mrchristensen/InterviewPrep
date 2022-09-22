# https://leetcode.com/problems/first-missing-positive/
# Runtime: 344 ms, faster than 89.99% of Python3 online submissions for First Missing Positive.
# Memory Usage: 27.3 MB, less than 89.10% of Python3 online submissions for First Missing Positive.

# 20 minutes

# Time Complexity: O(4n) = O(n)
# Space Complexity: O(1)

# Hash Key:
import queue
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        # Make sure 1 is in our list
        if(1 not in nums):
            return 1

        # Change anything negative or 0 to a one (so we can flip signs without collisions)
        for i in range(length):
            if(nums[i] < 1):
                nums[i] = 1

        # Change the index's of numbers in our list to negatives
        i = 0
        for i in range(length):
            if(1 <= abs(nums[i]) <= length):
                nums[abs(nums[i]) - 1] =  - abs(nums[abs(nums[i]) - 1])

        # Return the first index that has not be flipped negative (+1 on everything bc of 0 index)
        i = 0
        for i in range(length):
            if(nums[i] > 0):
                break
            else:
                i += 1
        return i + 1


# Sorting solution
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums.sort()
#         length = len(nums)
#         i = 0
#         expected_number = 1

#         # Get the index to where 1 is found
#         while i < length:
#             if(nums[i] > 0):
#                 break
#             i += 1

#         while i < length:
#             if(nums[i] == expected_number):
#                 i += 1
#                 expected_number += 1
#             elif(nums[i] == expected_number - 1):
#                 i += 1
#             elif(nums[i] != expected_number):
#                 break

#         return expected_number
