
# LeetCode #977 - Squares of a Sorted Array
# Day 7/60 - Two Pointers
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        index = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1

            index -= 1

        return result
