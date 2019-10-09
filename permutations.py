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