# Problem #46
# https://leetcode.com/problems/permutations
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],    
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        left = set(nums)
        perms = []
        for x in list(left):
            copy = left.copy()
            copy.remove(x)
            perms += [[x] + perm for perm in self.permute(list(copy))]
        return perms