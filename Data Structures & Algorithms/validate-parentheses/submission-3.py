class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }
        stack = []

        for c in s:
            if stack and c in closeToOpen:
                if stack[-1] != closeToOpen.get(c, 0):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False
