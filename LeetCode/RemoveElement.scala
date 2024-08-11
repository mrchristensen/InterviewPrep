// https://leetcode.com/problems/remove-element/
// Runtime: 595 ms, Beats 85.71%
// Memory: 56.64 MB, Beats 96.83%

// 10 minutes

// Time Complexity: O(n)
// Space Complexity: O(n)

object Solution {
    def removeElement(nums: Array[Int], value: Int): Int = {
        var i = 0
        var length = nums.length
        var j = length - 1

        while(i <= j){
            if(nums(i) == value){
                nums(i) = nums(j)
                j -= 1
                length -= 1
            }
            else{
                i += 1
            }
        }

        length
    }
}