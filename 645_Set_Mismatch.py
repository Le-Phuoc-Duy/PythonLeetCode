from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = {}
        repetitionNumber = 0 
        for idx, num in enumerate(nums):
            if num in visited:
                repetitionNumber = num
                break            
            visited[num] = idx
        n = len(nums)
        lossNumber = n*(n+1)//2 -sum(nums) + repetitionNumber
        return [repetitionNumber,lossNumber]  


            