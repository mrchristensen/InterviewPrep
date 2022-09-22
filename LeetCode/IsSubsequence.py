# https://leetcode.com/problems/is-subsequence/
# Runtime: 31 ms, faster than 95.89% of Python3 online submissions for Is Subsequence.
# Memory Usage: 13.8 MB, less than 82.25% of Python3 online submissions for Is Subsequence.

# 2 minutes

# Time Complexity: O(n) | n = length of t
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i_bound, j_bound = len(s), len(t)
        i, j = 0, 0
        while i < i_bound and j < j_bound:
            if(s[i] == t[j]):
                i += 1
            j += 1

        if(i == i_bound):
            return True
        return False
