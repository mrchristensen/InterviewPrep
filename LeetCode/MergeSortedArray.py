# https://leetcode.com/problems/merge-sorted-array/
# Runtime: 33ms, Beats 98.48%of users with Python3
# Memory: 16.24MB, Beats 82.23%of users with Python3

# 28 minutes

# Time Complexity: O(n + m)
# Space Complexity: O(2n + m) = O(n + m)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        length = m-1

        while(i < n+m and j < n):
            if(nums2[j] < nums1[i] or i > length):
                nums1.pop(-1)
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                length += 1
            else:
                i += 1
