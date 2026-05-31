# Use a stack to track opening brackets.
# If we see an opening bracket, push it onto the stack.
# If we see a closing bracket, check if it matches the top of the stack.
# If it matches, pop the opening bracket.
# At the end, the string is valid only if the stack is empty.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pMap:
                if stack and pMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        