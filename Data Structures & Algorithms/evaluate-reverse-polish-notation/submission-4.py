class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                if a//b < 0:
                    if a//b == a / b:
                        stack.append(a // b)
                    else:
                        stack.append(a//b + 1)
                else:
                    stack.append(a // b)
            else:
                stack.append(int(token))
        return stack[-1]