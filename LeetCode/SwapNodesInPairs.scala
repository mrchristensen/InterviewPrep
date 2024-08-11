// https://leetcode.com/problems/swap-nodes-in-pairs/
// Runtime: 608 ms, Beats 66.67%
// Memory: 59.76 MB, Beats 72.22%

// 15 minutes


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
    def swapPairs(head: ListNode): ListNode = {
        var node = head

        while(node != null && node.next != null){
            val temp = node.x

            node.x = node.next.x
            node.next.x = temp

            node = node.next.next
        }
        head
    }
}