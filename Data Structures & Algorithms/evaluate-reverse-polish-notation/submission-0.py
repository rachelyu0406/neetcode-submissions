class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                two = int(stack.pop())
                one = int(stack.pop())
                if token == "+":
                    stack.append(one + two)
                elif token == "-":
                    stack.append(one - two)
                elif token == "*":
                    stack.append(one * two)
                else:
                    stack.append(int(one / two))
        return int(stack[-1])   
