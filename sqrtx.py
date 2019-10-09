class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        #search for sqrt
        lo = 1

        hi = x // 2
        mid = (hi+1) // 2
        
        1 ,2,3, 4 ,5,6,7,8,(9)
        while lo < hi:
            mid = (hi+lo) // 2
            if (mid * mid) <= x and ((mid+1) * (mid+1)) > x:
                return mid
            elif mid * mid < x:
                lo = mid+1
                mid = hi
                
            else:
                hi = mid-1
                mid = lo
                
        return mid