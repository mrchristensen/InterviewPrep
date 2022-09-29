# https://leetcode.com/problems/roman-to-integer/submissions/

# 21 min

# Time Complexity: O(n) | n = len(s) (number of digits)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        end_of_string = 0
        total = 0
        length = len(s)

        # Go through each individual numeral
        for i in range(length):
            cur_value = roman_map[s[i]]  # Get the value from the map
            prox_value = roman_map[s[i + 1]] if i + 1 < length else end_of_string

            # If the current value is bigger than the next, we SUM it to the total (the V in VI equals +5)
            if(cur_value >= prox_value):
                total += cur_value
            # If the current value is smaller, we SUBTRACT it from the total (the I in IV equals -1)
            else:
                total -= cur_value

        return total
