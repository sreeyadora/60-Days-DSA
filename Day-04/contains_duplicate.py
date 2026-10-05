# LeetCode #217 - Contains Duplicate
# Day 4/60 - Time & Space Complexity
# Approach: Brute Force / Optimized
# Time Complexity: Add after choosing your approach
# Space Complexity: Add after choosing your approach
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False