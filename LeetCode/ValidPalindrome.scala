// https://leetcode.com/problems/valid-palindrome/
// Runtime: 842 ms, beats 73.68%
// Memory: 73.3 MB, beats 31.58%

// 10 minutes

// Time Complexity: O(n)
// Space Complexity: O(n)

object Solution {
    def isPalindrome(s: String): Boolean = {
        var sanitizedString = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        var start_index = 0;
        var end_index = sanitizedString.length() -1;

        while(start_index <= end_index){
            if(sanitizedString(start_index) != sanitizedString(end_index)){
                return false
            }
            start_index += 1;
            end_index -= 1;
        }
        
        return true;
    }
}
