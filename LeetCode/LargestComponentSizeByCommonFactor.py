# https://leetcode.com/problems/largest-component-size-by-common-factor/
# Runtime: 4507 ms, faster than 54.03% of Python3 online submissions for Largest Component Size by Common Factor.
# Memory Usage: 20.4 MB, less than 72.04% of Python3 online submissions for Largest Component Size by Common Factor.

# Too long, lol

# Time Complexity: O(n log n)
# Space Complexity: O(n)

class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]
        self.size = [1] * (size+1)

    def find(self, i):
        if(self.parent[i] != i):
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if(parent_i == parent_j):
            return parent_i
        if(self.size[parent_i] < self.size[parent_j]):
            parent_i, parent_j = parent_j, parent_i

        self.parent[parent_j] = parent_i
        self.size[parent_i] += self.size[parent_j]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        disjoint_set = DisjointSet(max(nums))

        for num in nums:
            for factor in range(2, int(sqrt(num))+1):
                if num % factor == 0:
                    disjoint_set.union(num, factor)
                    disjoint_set.union(num, num // factor)

        connected_components = {}
        for num in nums:
            group = disjoint_set.find(num)
            if group in connected_components:
                connected_components[disjoint_set.find(num)] += 1
            else:
                connected_components[disjoint_set.find(num)] = 1

        # print("connected_components:", connected_components)
        return max(connected_components.values())


# Times out:

# class Solution:
#     def __init__(self):
#         self.visited = set()
#         self.counter = 0
#         self.graph = {}


#     def gcd(self, a, b):
#         # Everything divides 0
#         if (a == 0):
#             return b
#         if (b == 0):
#             return a

#         # base case
#         if (a == b):
#             return a

#         # a is greater
#         if (a > b):
#             return gcd(a-b, b)
#         return gcd(a, b-a)


#     def dfs(self, node):
#         self.visited.add(node)
#         # print("Visited:", node)
#         self.counter += 1

#         # If we have no neighbors, return
#         if(node not in self.graph):
#             return

#         for neighbor in self.graph[node]:
#             if(neighbor not in self.visited):
#                 self.dfs(neighbor)


#     def largestComponentSize(self, nums: List[int]) -> int:
#         for num in nums:
#             self.graph[num] = set()

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 num1 = nums[i]
#                 num2 = nums[j]

#                 # If nums share a common factor greater than 1
#                 # if(self.gcd(num1, num2) > 1):
#                 if(self.gcd(num1, num2) > 1):
#                     self.graph[num1].add(num2)
#                     self.graph[num2].add(num1)

#         largest_num_cc = 0
#         for node in nums:
#             if(node not in self.visited):
#                 self.dfs(node)
#                 largest_num_cc = max(largest_num_cc, self.counter)
#                 self.counter = 0

#         return largest_num_cc
