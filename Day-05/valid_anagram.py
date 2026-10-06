
# LeetCode #242 - Valid Anagram
# Day 5/60 - Hash Maps & Sets
# Approach: Character Frequency
# Time Complexity: O(n)
# Space Complexity: O(1) for a fixed alphabet
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True