# https://leetcode.com/problems/palindrome-linked-list/submissions/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # A list with just one element is a palindrome
        if(head.next is None):
            return True
        
        start = head
        
        # Get second half of list and reverse it
        half = self.getHalfWayNode(start)
        reversed_half = self.reverseList(half)
        
        # Check the first half against the reversed second half
        while(reversed_half is not None):
            # If they are not equal it's not a palindrome
            if(start.val != reversed_half.val):
                return False
            start = start.next
            reversed_half = reversed_half.next
            
        return True
        
    
    def getHalfWayNode(self, node):     
        half = node
        end = node
        
        # Step two indices by one (slow) and two (fast) to find middle (when fast hits end, slow = middle)
        while(end.next is not None and end.next.next is not None):
            half = half.next
            end = end.next.next
            
        # Get the beginning of the second half (currently end of first half/exact middle entry if odd)
        half = half.next
            
        return half     
      
    # From LeetCode/ReverseLinkedList.py (https://leetcode.com/problems/reverse-linked-list/)
    def reverseList(self, head):      
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
        
#         # Old Solution:
#         # Find length of list
#         length = 0
#         node = head
#         while(node is not None):
#             length +=1
#             node = node.next
#         # print("Length:", length)
        
#         # Add first half to stack
#         index = 0
#         stack = []
#         node = head
#         while(index < length/2):
#             stack.append(node.val)
#             node = node.next
#             index += 1
        
#         # Pop the middle one (if needed)
#         if(length % 2 != 0):
#             stack.pop()
        
#         # Compare the second half to the top of the first half stack
#         while(node is not None):
#             if(stack.pop() != node.val):
#                     return False
#             node = node.next
            
#         return True
