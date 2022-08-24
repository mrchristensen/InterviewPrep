# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time Complexity: O(n) + O(log(n))
# Space Complexity: O(n + m)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:       
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2
        
        # Make nums1 the smaller list
        if(len1 > len2):
            nums1, nums2 = nums2, nums1
        
        # Merge nums1 into nums2
        for num in nums1:
            nums2 = self.mergeInsert(num, nums2)

        half_len = int(total_len / 2)
        
        # If we have an even list
        if(total_len % 2 == 0):
            return (nums2[half_len -1] + nums2[half_len]) / 2
        # If we have an odd list
        else:
            return nums2[half_len]
            
        
    def mergeInsert(self, num, nums):
        length = len(nums)
        
        if(length == 0):
            return [num]
        
        if(length == 1):
            if num < nums[0]:
                nums.insert(0, num)
                return nums
            else:
                nums.append(num)
                return nums
            
        half_index = int(length / 2)
        smaller = num <= nums[half_index]
        
        if smaller:
            return self.mergeInsert(num, nums[:half_index]) + nums[half_index:]
        else:
            return nums[:half_index] + self.mergeInsert(num, nums[half_index:])
        
            
                
