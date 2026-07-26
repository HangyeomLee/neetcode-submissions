class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        con_cnt = 1
        max_cnt = 1
        nums = sorted(nums)
        seen = set()
        nodup_nums = []
        if len(nums) == 0:
            return 0
        #eliminate duplicates
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nodup_nums.append(nums[i])

        for i in range(1,len(nodup_nums)):
            if nodup_nums[i] - 1 == nodup_nums[i-1]:
                con_cnt += 1
            else:
                max_cnt = max(max_cnt , con_cnt)
                con_cnt = 1
        max_cnt = max(max_cnt, con_cnt)
        return max_cnt

        #first, sorted the nums list and compare the values