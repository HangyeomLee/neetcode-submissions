class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i, num in enumerate(nums):
            if target - num in seen:
                res.append(seen[target - num])
                res.append(i)
                return res
            seen[num] = i