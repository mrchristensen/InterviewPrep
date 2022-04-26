# https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
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
            
            ret.append(entry)
        
        return ret
