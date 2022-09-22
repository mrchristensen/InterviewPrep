# https://leetcode.com/problems/reverse-string/
# Runtime: 196 ms, faster than 98.46% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 83.38% of Python3 online submissions for Reverse String.

# 5 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

        # Other option (takes up more memory)
        # s[::] = s[::-1]
