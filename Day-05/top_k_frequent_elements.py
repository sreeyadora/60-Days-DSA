# LeetCode #347 - Top K Frequent Elements
# Day 5/60 - Hash Maps & Sets
# Approach: Frequency Map + Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result