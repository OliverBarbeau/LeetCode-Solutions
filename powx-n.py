# Problem #50
# https://leetcode.com/problems/powx-n
# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 2147483647:
            if x >= 1:
                return x
            elif x == -1:
                return x
            return 0.0
        elif n == -2147483648:
            if x > 1:
                return 0.0
            elif x == 1 or x == -1:
                return 1.0
            return float('inf')
        product = 1
        while n > 0:
            product *= x
            n-=1
        while n < 0:
            product /= x
            n += 1
        return product