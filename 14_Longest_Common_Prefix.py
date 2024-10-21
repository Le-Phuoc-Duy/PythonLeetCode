from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for s in strs:
            if(len(s)<len(shortest)):
                shortest = s   
        while(len(shortest)>=0):
            flag = True 
            for s in strs:
                if not(s.find(shortest) == 0):
                    flag = False
                    break
            if flag:
                break
            else:
                shortest = shortest[0:len(shortest)-1]
        return shortest 