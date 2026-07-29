class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for target in s:
            if target == "[" or target == "{" or target == "(":
                stack.append(target)
            elif not stack:
                return False
            elif target == "]" and stack[-1] == "[":
                stack.pop()
            elif target == "}" and stack[-1] == "{":
                stack.pop()
            elif target == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
            