class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        if s[0] in myDict.keys():
            return False
        stack = []
        for i in s:
            if i in myDict.values():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != myDict[i]:
                    return False    
        return len(stack) == 0 