# https://leetcode.com/problems/first-unique-character-in-a-string/
# Runtime: 107 ms, faster than 85.99% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14 MB, less than 99.71% of Python3 online submissions for First Unique Character in a String.

# 12 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = {}
        repeated_letters = set()

        for i in range(len(s)):
            # If we haven't seen it before, save the index
            if(s[i] not in letter_map):
                letter_map[s[i]] = i
            # Else, add it to repeated letters that we've seen
            else:
                repeated_letters.add(s[i])

        for letter in letter_map:
            # If we haven't seen a repeat we found our answer (the dic is ordered)
            if(letter not in repeated_letters):
                return letter_map[letter]

        # Default return value
        return -1
