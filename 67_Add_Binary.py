class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumInDecimal = int(a,2) + int(b,2)
        return bin(sumInDecimal).replace("0b","") 
    