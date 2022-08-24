# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:       
        sorted_nums = []
        
        nums1_index, nums2_index = 0, 0
        nums1_length, nums2_length = len(nums1), len(nums2)        
        total_len = nums1_length + nums2_length
        
        # Add which ever number is smaller to the sorted list (until you run out of a list)
        while(nums1_index < nums1_length and nums2_index < nums2_length):
            if(nums1[nums1_index] < nums2[nums2_index]):
                sorted_nums.append(nums1[nums1_index])
                nums1_index += 1
            else:
                sorted_nums.append(nums2[nums2_index])
                nums2_index += 1
        # Finish off the other lists
        while(nums1_index < nums1_length):
            sorted_nums.append(nums1[nums1_index])
            nums1_index += 1
        while(nums2_index < nums2_length):
            sorted_nums.append(nums2[nums2_index])
            nums2_index += 1

        half_len = int(total_len / 2)
        
        # If we have an even list
        if(total_len % 2 == 0):
            return (sorted_nums[half_len - 1] + sorted_nums[half_len]) / 2
        # If we have an odd list
        else:
            return sorted_nums[half_len]
