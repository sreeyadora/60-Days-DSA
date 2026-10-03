# Day 1/60
# LeetCode #1480 - Running Sum of 1D Array
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        ans = []
        for num in nums:
            total = total+num
            ans.append(total)
        return ans
        