class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_map = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in check_map:
                if stack and stack[-1] == check_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        
        

        
