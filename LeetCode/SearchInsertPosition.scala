// https://leetcode.com/problems/search-insert-position/
// Runtime: 614 ms, Beats 86.36%
// Memory: 57.18 MB, Beats 95.45%

// 30 minutes

// Time Complexity: O(log n)
// Space Complexity: O(n)

object Solution {
    def searchInsert(nums: Array[Int], target: Int): Int = {
       var start = 0
       var end = nums.length - 1
       var middle = 0

       while(end - start > 1){
            middle = (start + end) / 2
            if(nums(middle) == target){
                return middle
            }
            else if(nums(middle) < target){
                start = middle
            }
            else{
                end = middle
            }
        }

        if(nums(start) >= target){
            return start
        }
        if(nums(end) >= target){
            return end
        }
        end + 1
    }
}