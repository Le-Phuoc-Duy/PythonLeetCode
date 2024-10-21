from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for idx, i in enumerate(nums):
            if target - i in tmp:
                return [idx, tmp[target - i]]
            tmp[i] = idx