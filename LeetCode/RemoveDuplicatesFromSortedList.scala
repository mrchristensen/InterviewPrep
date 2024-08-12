// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
// Runtime: 662 ms, Beats 72.22%
// Memory: 60.01 MB, Beats 61.11%

// 9 minutes

// Time Complexity: O(n)
// Space Complexity: O(n)

/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def deleteDuplicates(head: ListNode): ListNode = {
        var node = head
        while(node != null && node.next != null){
            if(node.x == node.next.x){
                node.next = node.next.next
            }
            else{
                node = node.next
            }
        }
        head
    }
}