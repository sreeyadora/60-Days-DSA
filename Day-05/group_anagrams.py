# LeetCode #49 - Group Anagrams
# Day 5/60 - Hash Maps & Sets
# Approach: Hash Map
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())