# LeetCode #169 - Majority Element
# Day 4/60 - Time & Space Complexity
# Approach: Brute Force / Optimized
# Time Complexity: Add after choosing your approach
# Space Complexity: Add after choosing your approach
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate =  num
            if num == candidate:
                count+=1
            else:
                count-=1
        return candidate
        