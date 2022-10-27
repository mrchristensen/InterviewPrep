// https://leetcode.com/problems/reverse-integer/
// Runtime: 495 ms, faster than 98.13% of Scala online submissions for Reverse Integer.
// Memory Usage: 51.9 MB, less than 89.72% of Scala online submissions for Reverse Integer.

// 30 minutes

// Time Complexity: O(n)
// Space Complexity: O(1) (because -2^31 <= x <= 2^31 - 1 constraint

object Solution {
    def reverse(x: Int): Int = {
        var num = x
        var reversedNum = ""
        val defaultReturn = 0

        // If negative, we prepend the "-" onto the string and remove it from the int
        if(num < 0){
            reversedNum = "-"
            num = num * -1
        }

        reversedNum += num.toString.reverse  // reverse time complexity: O(n)

        try {
            return reversedNum.toInt
        } catch {
            case e: NumberFormatException => return 0
        }

    }
}
