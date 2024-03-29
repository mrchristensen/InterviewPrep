# https://leetcode.com/problems/merge-two-sorted-lists/
# Runtime: 60 ms, faster than 48.20% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.8 MB, less than 98.84% of Python3 online submissions for Merge Two Sorted Lists.

# 30 minutes

# Time Complexity: O(n + m) | n, m = len(list1), len(list2)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        head = new_list

        # Point to the list with the smallest value (until we run out of one list)
        while(list1 and list2):
            if(list1.val < list2.val):
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next

        # Finish up remaining list
        new_list.next = list1 if list1 else list2

        return head.next
