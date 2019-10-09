class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1, 2:2}
        def _climbStairs(n):
            if n in d:
                return d[n]
            d[n] = _climbStairs(n-1) + _climbStairs(n-2)
            return d[n]
        return _climbStairs(n)