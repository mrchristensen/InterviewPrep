# https://leetcode.com/problems/fizz-buzz/

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :return type: List[str]
        """

        ret = []
        for i in range(1, n + 1):
            entry = ""
            if i % 3 == 0:
                entry += "Fizz"

            if i % 5 == 0:
                entry += "Buzz"

            if entry == "":
                entry = str(i)

            # This is faster for some reason
            ret.append(''.join(entry))

        return ret
