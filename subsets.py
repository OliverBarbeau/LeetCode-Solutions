class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            newSets = []
            for s in sets:
                newSets.append([num]+s)
            sets = sets + newSets
        return sets