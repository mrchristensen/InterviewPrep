# https://leetcode.com/problems/palindrome-number/

# 2 minutes

# Runtime 57ms, Beats 79.26%of users with Python3
# Memory 16.22MB, Beats 70.83%of users with Python3

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        digit_i = 0
        digit_j = len(num) - 1

        while(digit_i < digit_j):
            if(num[digit_i] != num[digit_j]):
                return False
            digit_i += 1
            digit_j -= 1
        return True
