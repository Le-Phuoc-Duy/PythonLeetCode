from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        if min(nums) == 1:
            return 0
        maxNumber = max(nums)
        check = maxNumber*(maxNumber+1)//2 - sum(nums)
        if check == 0:
            return maxNumber+1
        return check