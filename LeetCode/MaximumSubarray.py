import operator

# 1 hour 40 minutes

class Solution:
    def flipSign(self, op):
        if(op == operator.ge):
            return operator.le
        else:
            return operator.ge

    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        merged_nums = []
        op = operator.le if nums[0] < 0 else operator.ge
        biggest_total = 0
        total = 0
        for num in nums:
            if(op(num, 0)):
                total += num
            else:
                op = self.flipSign(op)
                merged_nums.append(total)
                total = num
        if(total != 0):
            merged_nums.append(total)

        # print(merged_nums)
        if(len(merged_nums) == 1):
            return merged_nums[0]

        # Get rid of ends if negative (we will never want them)
        if(merged_nums[0] < 0):
            merged_nums.pop(0)
        if(merged_nums[-1] < 0):
            merged_nums.pop(-1)

        # If we're down to one number, we're done
        if(len(merged_nums) == 1):
                return merged_nums[0]

        # print("merged_nums:", merged_nums)

        old_length = len(merged_nums)
        new_length = None
        i = 1
        while old_length != new_length:
            new_merged = []
            old_length = len(merged_nums)

            while i < old_length-1:
                # print("i:", i)
                # If the sum of the two positives with the negative is an improvement
                if(abs(merged_nums[i]) <= min(merged_nums[i-1], merged_nums[i+1])):
                    # print("Merging sum:", sum(merged_nums[i-1:i+2]))
                    new_merged.append(sum(merged_nums[i-1:i+2]))

                    i += 4
                    if(i == old_length):
                        new_merged.append(merged_nums[i-2])
                        new_merged.append(merged_nums[i-1])
                else:
                    # print("appending:", merged_nums[i-1:i+1])
                    new_merged.append(merged_nums[i-1])
                    new_merged.append(merged_nums[i])

                    i += 2
                    if(i >= old_length):
                        new_merged.append(merged_nums[i-1])

            # print("new_merged:", new_merged)
            merged_nums = new_merged
            new_length = len(merged_nums)
            i = 1

            if(len(merged_nums) == 1):
                return merged_nums[0]

        return max(merged_nums)
