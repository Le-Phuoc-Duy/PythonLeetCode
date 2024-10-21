class Solution: 
    def isIsomorphic(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return False
        mapDict = {}
        tmp = ""
        for idx,c in enumerate(s):
            if c not in mapDict:
                mapDict[c] = t[idx]
                tmp += t[idx]
            else: 
                tmp += mapDict[c] 
        if len(set(mapDict.values())) != len(list(mapDict.values())):
            return False
        return tmp == t 
    
 