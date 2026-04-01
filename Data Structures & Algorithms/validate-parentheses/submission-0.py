class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkMap = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in checkMap:
                if stack and stack[-1] == checkMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
        

        
