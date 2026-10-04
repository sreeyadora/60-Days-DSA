# LeetCode #1672 - Richest Customer Wealth
# Day 2/60
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth=0
            for money in customer:
                wealth+=money
            max_wealth=max(max_wealth,wealth)
        return max_wealth
        