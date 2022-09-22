# https://leetcode.com/problems/merge-k-sorted-lists
# Runtime: 174 ms, faster than 51.08% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18 MB, less than 45.54% of Python3 online submissions for Merge k Sorted Lists.

# 27 minutes

# Time Complexity: O(N log n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Priority Queue Impl
import queue

class PQItem:
    def __init__(self, num, node):
        self.num: int
        item: Any=field(compare=False)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        max = 10001
        merged_list = ListNode()
        current_node = merged_list
        pq = queue.PriorityQueue(len(lists))

        # Add initial elements to the queue
        for i in range(len(lists)):
            node = lists[i]
            if node:
                pq.put((node.val, i))
                lists[i] = node.next


        while(pq.empty() == False):
            val, i = pq.get()

            current_node.next = ListNode(val)
            current_node = current_node.next

            # If there is another value
            node = lists[i]
            if node:
                pq.put((node.val, i))
                lists[i] = node.next

        return merged_list.next


# Initial Impl
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         max = 10001
#         lists = list(filter(None, lists))  # Remove empty lists
#         merged_list = ListNode()

#         current_node = merged_list
#         while(len(lists) > 0):
#             lowest_val = max
#             lowest_list = None

#             # Find the lowest exposed value in the lists
#             for k in range(len(lists)):
#                 # print("k,",k)
#                 if(lists[k].val < lowest_val):
#                     lowest_val = lists[k].val
#                     lowest_list = k

#             # Add the lowest value to the final list
#             # print("Adding lowest_val to list:", lowest_val)
#             current_node.next = ListNode(lowest_val)
#             current_node = current_node.next

#             # Move to the next element in the lowest list (or remove list if no more elements)
#             if(lists[lowest_list].next == None):
#                 lists.pop(lowest_list)
#             else:
#                 lists[lowest_list] = lists[lowest_list].next

#         return merged_list.next
