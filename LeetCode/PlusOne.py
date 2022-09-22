# https://leetcode.com/problems/plus-one/
# Runtime: 31 ms, faster than 96.65% of Python3 online submissions for Plus One.
# Memory Usage: 13.7 MB, less than 99.78% of Python3 online submissions for Plus One.

# 8 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        digits[index] += 1

        while digits[index] == 10:
            digits[index] = 0
            index -= 1
            if(index < 0):
                digits.insert(0, 1)
            else:
                digits[index] += 1

        return digits
