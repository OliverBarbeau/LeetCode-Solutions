class Solution:
    def reverse(self, x):
        signed = False
        if x < 0:
            signed = True
            x = -x
        num = 0
        while (x != 0):
            num *= 10
            num = int(num + (x % 10))
            x = int(x / 10)
        if (abs(num) > (1 << 31) - 1):
            return 0
        if (signed):
            return -1*num
        else:
            return num