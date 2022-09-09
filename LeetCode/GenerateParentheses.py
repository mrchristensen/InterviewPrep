# https://leetcode.com/problems/generate-parentheses/    

# 1 hour 20 minutes

# On-the-Fly Branch-and-Bound:
# Runtime: 30 ms, faster than 98.64% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.1 MB, less than 77.00% of Python3 online submissions for Generate Parentheses.

# Time Complexity: O(4^n)
# Space Complexity: O(4^n)

class Solution:
    def __init__(self):
        self.combos = []
    
    def generateParenthesis(self, n: int, op = 0, cp = 0, string = "") -> List[str]:
        while(True):
            if(cp == n):
                self.combos.append(string)
                break
            print("n, op, cp, string:", n, op, cp, string)
            # if open == max: have to close
            if(op == n):
                print(open == max)
                string += ")"
                cp += 1
            # elif open == closed: have to open
            elif(op == cp):
                print("open == closed")
                string += "("
                op += 1
            # else: do both
            else:
                print("Do both")
                self.generateParenthesis(n, op + 1, cp, str(string + "("))
                self.generateParenthesis(n, op, cp + 1, str(string + ")"))
                break
            
        return self.combos

# Dynamic Programming:
# Runtime: 35 ms, faster than 94.58% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.5 MB, less than 5.42% of Python3 online submissions for Generate

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# import itertools
# class Solution:
#     def __init__(self):
#         self.combos = []
    
#     def generateParenthesis(self, n: int, op = 0, cp = 0, string = "") -> List[str]:
#         sol_map = {}
        
#         # Combos for 1
#         sol_map[1] = {"()"}

#         # Build combos from 2 to n
#         for i in range(2,n+1):
#             i_combos = set()
            
#             # Find relevant sums:
#             sums = set()
#             for j in range(1,i):
#                 if(j not in sums):
#                     reciprocal = i - j
#                     sums.add(j)
#                     sums.add(j)
#                     i_combos = i_combos.union(self.getCombos(sol_map[j], sol_map[reciprocal]))        
                
#             # Previous combo, but wrapped
#             for prev_combo in sol_map[i-1]:
#                 i_combos.add("(" + prev_combo + ")")

#             sol_map[i] = i_combos
        
#         return sol_map[n]

#     def getCombos(self, list1, list2):
#         s = set()
#         for product in itertools.product(list1, list2):
#             for perms in itertools.permutations(product):
#                 s.add(perms[0] + perms[1])
        
#         return s
