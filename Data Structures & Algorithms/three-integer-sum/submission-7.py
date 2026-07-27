class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        lp = 0
        rp = len(nums) - 1
        answer = []
        nums = sorted(nums)
        cnt = len(nums) - 1
        for i in range(length):
            lp = i + 1
            rp = length - 1
            if nums[i] == nums[i-1] and i > 0:
                continue
            while lp < rp:
                target = nums[lp] + nums[rp]
                if nums[i] + target == 0:
                    answer.append([nums[i],nums[lp],nums[rp]])
                    lp = lp + 1
                    rp = rp - 1
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp+1]:
                        rp -= 1
                elif nums[i] + target > 0:
                    rp = rp - 1
                else:
                    lp = lp + 1

                
        return answer
