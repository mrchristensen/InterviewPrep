# https://leetcode.com/problems/two-sum/

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        complements = {}

        for num in nums:
            if(num in complements):
                return [complements[num], index]
            else:
                complements[target - num] = index

            index += 1
