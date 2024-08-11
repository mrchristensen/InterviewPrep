// https://leetcode.com/problems/length-of-last-word/
// Runtime: 540 ms, Beats 91.67%
// Memory: 56.17 MB, Beats 65.48%

// 3 minutes

// Time Complexity: O(n)
// Space Complexity: O(n)


object Solution {
    def lengthOfLastWord(s: String): Int = {
        s.split(" ").lastOption.get.length
    }
}