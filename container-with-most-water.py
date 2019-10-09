class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        l = 0
        r = len(height) - 1
        
        while r > l:
            area = (r-l) * min(height[l], height[r])
            m = max(m, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m