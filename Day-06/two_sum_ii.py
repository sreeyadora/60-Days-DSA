# LeetCode #167 - Two Sum II - Input Array Is Sorted
# Day 6/60 - Two Pointers
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1

        while left<right:
            total = numbers[left]+numbers[right]

            if total==target:
                return[left+1, right+1]

            elif total<target:
                left+=1
            else:
                right-=1
        