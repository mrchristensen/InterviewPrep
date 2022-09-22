# https://leetcode.com/problems/power-of-three/

# Time Complexity: O(?) (whatever the math.log10() function costs)
# Space Complexity: O(1)

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n <= 0):
            return False

        return (math.log10(n)/math.log10(3)) % 1 == 0
