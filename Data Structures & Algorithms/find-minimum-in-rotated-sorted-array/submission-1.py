class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums) - 1 # last index 
        l = 0
        r = length
        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            
