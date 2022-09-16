# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime: 2659 ms, faster than 14.03% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 27.2 MB, less than 63.47% of Python3 online submissions for Kth Largest Element in an Array.

# 22 minutes

# Time Complexity: O(n log k)
# Space Complexity: O(n)

import queue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kList = queue.PriorityQueue(k)
        kList.put(nums[0])
        
        # O(n)
        for num in nums[1:]:
            smallest = kList.get()
            kList.put(smallest)
            
            # If we found a bigger value
            if(kList.full() == False or num > smallest):            
                # If we are full, pop the lowest element
                if(kList.full()):
                    kList.get()
                # O(log k) 
                kList.put(num)
                
        return kList.get()
