class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        loc = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi and loc == -1:
            mid = (hi+lo)//2
            if nums[mid] == target:
                loc = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        lo, hi = loc, loc
        while lo > 0 and nums[lo] == nums[lo-1]:
            lo -= 1
        while hi != -1 and hi < len(nums)-1 and nums[hi] == nums[hi+1]:
            hi += 1
        return [lo, hi]