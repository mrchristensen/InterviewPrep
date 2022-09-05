# https://leetcode.com/problems/longest-common-prefix/
# Runtime: 30 ms, faster than 98.39% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.8 MB, less than 88.34% of Python3 online submissions for Longest Common Prefix.

# 40 minutes

# Time Complexity: O(n x m) | n = how many string, m = length of shortest string
# Space Complexity: O(m)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        key = strs[0]
        longest_prefix = len(key)
        
        for string in strs[1:]:
            while(key[:longest_prefix] != string[:longest_prefix]):
                longest_prefix -= 1
                if(longest_prefix == 0):
                    return ""
        
        return key[:longest_prefix]

# 12 minutes
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         i = 0
        
#         while True:
#             for string in strs:
#                 if(i >= len(string) or string[i] != strs[0][i]):
#                     return strs[0][:i]
#             i += 1
