class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        index = (l + r)//2
        for i in range(len(nums)):
            index = (l + r)//2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                r = index
            else:
                l = index
        return -1