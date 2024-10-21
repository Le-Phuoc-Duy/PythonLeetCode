from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        _dict = {}
        for i,num in enumerate(nums): 
            if (num in _dict) and abs(_dict[num] - i)<= k:
                return True
            _dict[num] = i
        return False 