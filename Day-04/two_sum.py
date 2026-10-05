# LeetCode #1 - Two Sum
# Day 4/60 - Time & Space Complexity
# Approach: Brute Force / Optimized
# Time Complexity: Add after choosing your approach
# Space Complexity: Add after choosing your approach
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        