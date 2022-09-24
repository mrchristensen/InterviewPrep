# https://leetcode.com/problems/merge-intervals/
# Runtime: 153 ms, faster than 93.69% of Python3 online submissions for Merge Intervals.
# Memory Usage: 18.1 MB, less than 85.00% of Python3 online submissions for Merge Intervals.

# 42 minutes

# Time Complexity: O(n log n + n) = O(n log n)
# Space Complexity: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0]) # O(n log n)
        merged_intervals = []
        current_interval = sorted_intervals[0]

        length = len(sorted_intervals)
        for i in range(1, len(intervals)):  # O(n)
            next_interval = sorted_intervals[i]

            if(next_interval[0] <= current_interval[1]):
                if(current_interval[1] < next_interval[1]):
                    # We merge intervals with new, extended, range
                    current_interval[1] = next_interval[1]
            else:
                # We can't combine, so we'll add it to our final list
                merged_intervals.append(current_interval)
                current_interval = next_interval

        merged_intervals.append(current_interval)
        return merged_intervals
