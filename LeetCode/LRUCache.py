# https://leetcode.com/problems/lru-cache/

# 28 min intitial, 1hr 25 with linked list

# Time Complexity: O(1)
# Space Complexitu: O(n)

# Runtime: 1171 ms, faster than 65.07% of Python3 online submissions for LRU Cache.
# Memory Usage: 75 MB, less than 85.82% of Python3 online submissions for LRU Cache.

# Sorted dictionary solution:
from collections import OrderedDict

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = OrderedDict()
        

    def get(self, key: int) -> int:
        result = self.dictionary.get(key, -1)  # -1 if not found
        
        if(result != -1):
            self.dictionary.move_to_end(key)
        
        return result
        

    def put(self, key: int, value: int) -> None:         
        self.dictionary[key] = value
        self.dictionary.move_to_end(key)
        
        if(len(self.dictionary) > self.capacity):
            self.dictionary.popitem(False)
            
            
#Linked list solution:

# class DoubleLinkedNode():
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.next = None
#         self.previous = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.node_cache = {}
#         self.head, self.tail = DoubleLinkedNode(), DoubleLinkedNode()
#         self.head.previous = self.tail
#         self.tail.next = self.head


#     def get(self, key: int) -> int:
#         # If we don't have that key, return -1
#         if key not in self.node_cache: # O(1) lookup
#             return -1
        
#         # Else:
        
#         # Update the linked list and cache
#         node = self.node_cache[key]
#         self.removeNode(node)
#         self.addNode(node)       
        
#         # Return the value 
#         return node.value        


#     def put(self, key: int, value: int) -> None:         
#         # Remove node if we need to update the value
#         if key in self.node_cache: # O(1) lookup
#             self.removeNode(self.node_cache[key])
#             self.node_cache.pop(key)
        
#         # Check to see if we are at capacity
#         if len(self.node_cache) == self.capacity:
#             oldest_node = self.tail.next
            
#             self.node_cache.pop(oldest_node.key)
#             self.removeNode(oldest_node)
            
#         # Add node
#         node = DoubleLinkedNode(key, value)
#         self.addNode(node)
#         self.node_cache[key] = node
        
         
#     def removeNode(self, node):
#         # Get the nodes links
#         old_prev = node.previous
#         old_next = node.next
        
#         # Connect the neighbour nodes to nodes links
#         old_next.previous = old_prev
#         old_prev.next = old_next
        
    
#     def addNode(self, node):
#         # Grab old leader
#         old_head = self.head.previous

#         # Make node point to head and old leader
#         node.next = self.head
#         node.previous = old_head
        
#         # Make leader our node
#         self.head.previous = node
        
#         # Make old leader point to our node
#         old_head.next = node
