# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0
        
        best_length = 0
        index = 0
        
        letters = {}
        
        # print("String:", s)
        
        ## Scan across string until we repeate
        for char in s:
            if char in letters:
                break
            else:
                letters[char] = index
                best_length += 1
                index += 1
        
        # See if a different substring we found best our previous best
        length = self.lengthOfLongestSubstring(s[letters[char] + 1:])  # Snip string off at repeating letter
        if(length > best_length):
            best_length = length
            
        return(best_length)
