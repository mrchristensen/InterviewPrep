# https://leetcode.com/problems/3sum/
# Times out

# 1 hour

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        triplets = set()
        zeros = 0
        
        pos_nums, neg_nums = [] , []
        for num in nums:
            if(num < 0):
                neg_nums.append(num)
            else:
                pos_nums.append(num)
            
        for num in pos_nums:
            if(num == 0):
                zeros += 1
            triplets = triplets.union(self.twoSum(-num, neg_nums))
        # print("triplets after pos_nums:", triplets)
        
        if(zeros >= 3):
            triplets.add((0,0,0))
        
        for num in neg_nums:
            triplets = triplets.union(self.twoSum(-num, pos_nums))
        # print("triplets after neg_nums:", triplets)
        
        return triplets
    
    def twoSum(self, goal, nums):
        # print("Two sum for goal of:", goal)
        # print("nums:", nums)
        needed_nums = []
        triplets = set()
        for num in nums:
            if(num in needed_nums):
                triplets.add(tuple(sorted((-goal, num, goal - num))))
                # print("we found a (completed a set)", num, "triplets now:", triplets)
            elif(abs(num) <= abs(goal)):
                needed_nums.append(goal-num)
                # print("we found a (not enough)", num, "needed_nums now:", needed_nums)
                
        # print("Two sum for goal of:", goal, "Found triplets:", triplets)
        return triplets
        
