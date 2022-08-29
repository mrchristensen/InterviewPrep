# https://leetcode.com/problems/valid-parentheses/
# Runtime: 29 ms, faster than 96.84% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 98.20% of Python3 online submissions for Valid Parentheses.
    
# 1 hour

# Time Complexity: O(n)
# Space Complexity: O(n)

# Stack Solution:
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        open_pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        for char in s:
            if char in open_pairs:
                stack.append(char)
            elif(len(stack) == 0 or open_pairs[stack.pop()] != char):
                return False
        
        if len(stack) == 0:
            return True
        

# # Zipper Solution:
# class Solution:

#     def isValid(self, s: str) -> bool:
#         closed_pairs = {
#             ")": "(",
#             "]": "[",
#             "}": "{"
#         }
#         found_closed = False
#         closed_index = 0
#         open_index = 0
#         string = s
        
#         while i < len(string):     
#             char = string[i]
            
#             # If we are looking for a closing bracket
#             if(found_closed == False):
#                 if(char in closed_pairs):
#                     found_closed = True
#                 else:
#                     i += 1
                    
#             # We found closed, now looking for opening
#             if(found_closed == True):
#                 if(string[i - 1] == closed_pairs[char] and i - 1 >= 0):
#                     string = string[:i - 1] + string[i + 1:]
#                     i -= 1
#                     found_closed = False
#                 else:
#                     return False
        
        

#         if(string == ""):
#             return True
#         else:
#             return False
        
