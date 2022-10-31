// https://leetcode.com/problems/toeplitz-matrix/
// Runtime: 628 ms, faster than 100.00% of Scala online submissions for Toeplitz Matrix.
// Memory Usage: 54.2 MB, less than 100.00% of Scala online submissions for Toeplitz Matrix.

// 26 minutes

// Time Complexity: O(n x m) | n = matrix.length, m = matrix(0).length
// Space Complexity: O(1)

object Solution {
    def isToeplitzMatrix(matrix: Array[Array[Int]]): Boolean = {
        val len_y = matrix.length;
        val len_x = matrix(0).length;
        var x = 0;
        var y = len_y - 1;

        // Traverse first column
        while(y > 0){
            val value = matrix(y)(x);

            // Check diagonals
            var temp_x = x + 1;
            var temp_y = y + 1;
            while(temp_x < len_x && temp_y < len_y){
                if(matrix(temp_y)(temp_x) != value){
                    return false;
                }
                temp_x += 1;
                temp_y += 1;
            }
            y -= 1;
        }

        // Traverse first row
        while (x < len_x){
            val value = matrix(y)(x)

            // Check diagonals
            var temp_x = x + 1;
            var temp_y = y + 1;
            while(temp_x < len_x && temp_y < len_y){
                if(matrix(temp_y)(temp_x) != value){
                    return false;
                }
                temp_x += 1;
                temp_y += 1;
            }
            x += 1;
        }

        // If we made it here we traversed entire matrix and everything matches
        return true;
    }

}
