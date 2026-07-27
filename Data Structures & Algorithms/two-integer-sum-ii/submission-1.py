class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        answer = []
        for i, num in enumerate(numbers):
            if target - num in seen:
                answer.append(seen[target-num]+1)
                answer.append(i+1)
                return answer
            seen[num] = i 