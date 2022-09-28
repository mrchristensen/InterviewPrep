# https://leetcode.com/problems/trapping-rain-water/
# Runtime: 181 ms, faster than 64.26% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 20.4 MB, less than 7.06% of Python3 online submissions for Trapping Rain Water.

# 3 Hours

# Time Complexity: O(n)
# Space Complexity: O(n)

# Two Pointers Impl:
class Solution:

    def trap(self, height: List[int]) -> int:
        agua = 0
        left_max, right_max = 0, 0
        left = 0
        right = len(height) - 1
        while(left < right):
            if(height[left] > left_max):
                left_max = height[left]
            if(height[right] > right_max):
                right_max = height[right]

            if(left_max < right_max):
                agua += max(0, left_max - height[left])
                left += 1
            else:
                agua += max(0, right_max - height[right])
                right -= 1

        return agua

# # LinkedList Impl:
# class Node:
#     def __init__(self, index, height):
#         self.index = index
#         self.height = height
#         self.previous_node = None
#         self.next_node = None


# class Solution:

#     def append(self, node, tail):
#         old_last_node = tail.previous_node

#         node.previous_node = old_last_node
#         node.next_node = tail

#         old_last_node.next_node = node
#         tail.previous_node = node

#     def deleteNode(self, node):
#         old_prev = node.previous_node
#         old_next = node.next_node

#         old_prev.next_node = old_next
#         old_next.previous_node = old_prev

#     def trap(self, height: List[int]) -> int:
#         if(len(height) <= 2):
#             return 0

#         agua, peaks = 0, 0

#         # For bounds
#         height.insert(0, 0)
#         height.append(0)

#         # Peaks LinkedList
#         head, tail = Node(None, None), Node(None, None)
#         head.next_node = tail
#         tail.previous_node = head

#         # Final all peaks (local optima)
#         for i in range(1, len(height) - 1):
#             point = height[i]
#             if(height[i - 1] <= point >= height[i + 1]):
#                 self.append(Node(i, point), tail)
#                 peaks += 1

#         # Remove peaks that are in valleys
#         node = head.next_node.next_node

#         if(peaks >= 3):
#             # Go through all peaks
#             while (node.next_node.height != None):
#                 # If peak is below its neighboring peaks, remove it
#                 if(node.previous_node.height >= node.height <= node.next_node.height):
#                     self.deleteNode(node)
#                     changed = True
#                     peaks -= 1

#                     #If we can backup, we should
#                     if(node.previous_node.previous_node.index != None):
#                         node = node.previous_node
#                         continue
#                 node = node.next_node

#         # Find how much water we can fill between the peaks
#         water_line = 0
#         node = head.next_node
#         while (node.next_node.height != None):
#             i = node.index
#             j = node.next_node.index
#             water_line = min(height[i], height[j])

#             while(i < j):
#                 agua += max(0, water_line - height[i])
#                 i += 1

#             node = node.next_node

#         return agua


# Old solution (doesn't work, fails some test cases
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         optima_1, optima_2, agua, water_level_to_tallest_point_tiles = 0, 0, 0, 0
#         valley_tiles, valley_height = 0, 0
#         tallest_point = 0
        
#         print("height before:", height)
        
#         # For bounds
#         height.insert(0, 0)
#         height.append(0)

#         print("height after:", height)

#         for i in range(1, len(height) - 1):
#             print("i:", i, "height[i]:", height[i])
#             # If we find a local optima
#             point = height[i]
#             peaks = []
            
#             if(point >= height[i - 1] and point >= height[i + 1]):
                
#                 print("found a peak")                             
#                 optima_1 = optima_2
#                 optima_2 = height[i]
#                 # Water line at the lowest of the two peaks
#                 water_line = min(optima_1, optima_2)
                
#                 agua += (water_line * valley_tiles) - valley_height
                
#                 # If we find that our local optima it in a valley between two peak, we'll want the water
#                 # +1 for previous peak that is now part of a valley (and thus not previously counted)
#                 water_level_to_tallest_point_tiles += (tallest_point - water_line) * (valley_tiles)
#                 valley_tiles, valley_height = 0, 0
                
#                 # If this local optima is the tallest peak we've seen so far
#                 if(point > tallest_point):
#                     print("We found a new tallest point")
#                     print("Adding:", water_level_to_tallest_point_tiles, "to water")
#                     # Move water line to previous tallest point
#                     agua += water_level_to_tallest_point_tiles
#                     water_level_to_tallest_point_tiles = 0
                    
#                     # Update tallest point
#                     tallest_point = point
#                 # else:
#                 #     pass
#             else:
#                 valley_tiles += 1
#                 valley_height += height[i]
                
#         return agua
