# https://leetcode.com/problems/trapping-rain-water/
# Runtime: 181 ms, faster than 64.26% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 20.4 MB, less than 7.06% of Python3 online submissions for Trapping Rain Water.

# 3 Hours

# Time Complexity: O(n^2)?
# Space Complexity: O(n)

class Node:
    def __init__(self, index, height):
        self.index = index
        self.height = height
        self.previous_node = None
        self.next_node = None
            
        
class Solution:
    
    def append(self, node, tail):
        old_last_node = tail.previous_node
        
        node.previous_node = old_last_node
        node.next_node = tail
        
        old_last_node.next_node = node
        tail.previous_node = node
        
    def deleteNode(self, node):
        old_prev = node.previous_node
        old_next = node.next_node
        
        old_prev.next_node = old_next
        old_next.previous_node = old_prev
    
    def trap(self, height: List[int]) -> int:
        if(len(height) <= 2):
            return 0
        
        agua, peaks = 0, 0
        
        # For bounds
        height.insert(0, 0)
        height.append(0)
        
        # Peaks LinkedList
        head, tail = Node(None, None), Node(None, None)
        head.next_node = tail
        tail.previous_node = head

        # Final all peaks (local optima)
        for i in range(1, len(height) - 1):
            point = height[i]            
            if(point >= height[i - 1] and point >= height[i + 1]):
                new_node = Node(i, point)
                self.append(new_node, tail)
                peaks += 1
        
        # Remove peaks that are in valleys
        changed = True
        while(changed):
            changed = False
            node = head.next_node.next_node
            
            if(peaks <= 2):
                break
            
            # Go through all peaks
            while (node.next_node.height != None):
                # If peak is below its neighbouring peaks, remove it
                if(node.previous_node.height >= node.height <= node.next_node.height):
                    self.deleteNode(node)
                    changed = True
                    peaks -= 1
                node = node.next_node
            
        # Find how much water we can fill between the peaks
        water_line = 0
        node = head.next_node
        while (node.next_node.height != None):
            i = node.index
            j = node.next_node.index
            water_line = min(height[i], height[j])
            
            while(i < j):
                agua += max(0, water_line - height[i])
                i += 1
                
            node = node.next_node
                
        return agua
        
