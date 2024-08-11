# https://leetcode.com/problems/add-two-numbers/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode()
        current_digit = sum_list
        carried_digit = 0
        prev = None

        # Sum lists while there are digits from both lists
        while(l1 != None or l2 != None or carried_digit > 0):
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            digit_sum = l1val + l2val + carried_digit

            # If we need to carry a digit
            if(digit_sum >= 10):
                digit_sum -= 10
                carried_digit = 1
            else:
                carried_digit = 0

            current_digit.val = digit_sum

            # Bump all the linked lists down a digit
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev = current_digit # For removing the last
            current_digit.next = ListNode()
            current_digit = current_digit.next

        # Fixed dangling empty ListNode ("0") at end of list
        prev.next = None

        return sum_list
