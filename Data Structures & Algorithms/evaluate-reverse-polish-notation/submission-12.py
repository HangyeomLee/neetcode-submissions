class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set("+-*/")
        for token in tokens:
            if token in operator:
                b = stack.pop()
                a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if a//b > 0 or a//b == a/b:
                    stack.append(a // b)
                else:
                    stack.append(a//b + 1)
            else:
                stack.append(int(token))
        return stack[-1]