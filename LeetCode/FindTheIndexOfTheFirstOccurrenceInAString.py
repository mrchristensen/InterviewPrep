# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Runtime 39 ms Beats 67.18%
# Memory 16.2 MB Beats 47.92%

# 4 minutes

# Time Complexity: O(n^m) | n = len(haystack), m = len(needle)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:    
        needle_length = len(needle)  

        for i in range(len(haystack)-needle_length+1):
            if(haystack[i] == needle[0]):
                if(haystack[i:i+needle_length] == needle):
                    return i
        return -1
