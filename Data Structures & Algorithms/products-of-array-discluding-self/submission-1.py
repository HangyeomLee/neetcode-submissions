class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = []
        right_mul = []
        answer = []
        mul = 1
        for num in nums:
            left_mul.append(mul)
            mul *= num
        mul = 1
        for i in range(len(nums)-1 ,-1,-1):
            right_mul.append(mul)
            mul *= nums[i]
        for i in range(len(nums)):
            answer.append(left_mul[i]*right_mul[len(nums)-i-1])
        return answer