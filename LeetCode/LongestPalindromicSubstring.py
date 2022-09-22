# https://leetcode.com/problems/longest-palindromic-substring/
# Runtime: 757 ms, faster than 78.42% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14 MB, less than 58.93% of Python3 online submissions for Longest Palindromic Substring.

# 22 minutes

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0]
        for i in range(1,len(s)-1):
            if(s[i-1] == s[i+1]):
                palindrome = self.extendPalindrome(i-1, i+1, s)
                max_palindrome = palindrome if len(palindrome) > len(max_palindrome) else max_palindrome
            if(s[i-1] == s[i]):
                palindrome = self.extendPalindrome(i-1, i, s)
                max_palindrome = palindrome if len(palindrome) > len(max_palindrome) else max_palindrome

        if(s[len(s)-1] == s[len(s)-2]):
                palindrome = self.extendPalindrome(len(s)-1, len(s)-2, s)
                max_palindrome = palindrome if len(palindrome) > len(max_palindrome) else max_palindrome

        return max_palindrome

    def extendPalindrome(self, i, j, s):
        while(0 <= i-1 and j+1 < len(s)):
            if(s[i-1] == s[j+1]):
                i -= 1
                j += 1
            else:
                break

        return s[i:j+1]
