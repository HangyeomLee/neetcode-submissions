class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        result = [0 for _ in temperatures]
        for index in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[index]:
                curr = stk.pop()
                result[curr] = index - curr
            stk.append(index)
        return result