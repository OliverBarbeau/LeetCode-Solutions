# Problem #78
# https://leetcode.com/problems/subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            newSets = []
            for s in sets:
                newSets.append([num]+s)
            sets = sets + newSets
        return sets