class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left<right:
            mid = left + (right - left) // 2
            if(mid<=x/mid):
                left = mid + 1
            else:
                right = mid
        return right - 1 