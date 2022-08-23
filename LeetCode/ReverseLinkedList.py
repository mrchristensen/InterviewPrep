# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check for head being a list
        if(head is None):
            return head
        
        prev = None
        node = head
        
        # Reverse the direction of each node
        while(node.next is not None):
            next_node = node.next           
            node.next = prev

            prev = node
            node = next_node

        # Last node needs to be reversed
        node.next = prev
        
        return node
    
