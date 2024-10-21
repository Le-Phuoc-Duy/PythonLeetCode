from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = len(digits) - 1
        while(t>=0):
            if digits[t] != 9:
                digits[t] = int(digits[t]) + 1
                break
            digits[t] = 0
            if t == 0:
                digits.insert(0,1)
            t = t - 1
        return digits
    
sol = Solution()
d = [9,9,9]
print (sol.plusOne(d))