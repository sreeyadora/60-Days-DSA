# LeetCode #26 - Remove Duplicates from Sorted Array
# Day 10/60
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1