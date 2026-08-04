class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        target = 0
        for i in range(len(temperatures)):
            target = temperatures[i]
            cnt = 0
            for j in range(i,len(temperatures)):
                if temperatures[j]>target:
                   result.append(cnt)
                   break
                else:
                    cnt += 1
                    if j == len(temperatures) - 1:
                        result.append(0)
            
        return result
