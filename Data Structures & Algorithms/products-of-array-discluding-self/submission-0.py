class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        mul_sum = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                mul_sum *= num
        if zero_count >= 2:
            for i in range(len(nums)):
                nums[i] = 0
        elif zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = mul_sum
                else:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = mul_sum // nums[i]
        return nums

            

#if number of 0 is more than 2, every value is zero
#if number of 0 is one, every value except one is zero
#other wise mul/i index val is the answer