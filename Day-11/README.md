# Day 11 — Triplets with Smaller Sum 🚀

## Topics Covered
- Arrays and sorting
- Two Pointer technique
- Counting valid triplets
- Optimizing nested-loop solutions

## Problem
**Triplets with Smaller Sum — GeeksforGeeks**

Given an array of distinct integers and a target sum, count the unique triplets whose sum is strictly less than the target.

## Approach
1. Sort the array.
2. Fix one element using a loop.
3. Use left and right pointers to find valid pairs.
4. When the sum is smaller than the target, add `right - left` to the count.

## Complexity
- Time Complexity: O(n²)
- Auxiliary Space: O(1), excluding sorting

## Key Learning
Sorting and two pointers can count valid triplets efficiently without checking every possible combination.

## Progress
- Day: 11/60
- Platform: GeeksforGeeks
- Status: Completed after testing ✅