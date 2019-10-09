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