# https://leetcode.com/problems/isomorphic-strings/submissions
# Runtime: 62 ms, faster than 59.36% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.1 MB, less than 88.68% of Python3 online submissions for Isomorphic Strings.

# 20 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        for i in range(len(s)):
            if(s[i] not in mapping):
                if(mapping.items and t[i] in mapping.values()):
                    return False
                mapping[s[i]] = t[i]

            if(mapping[s[i]] != t[i]):
                return False

        return True
