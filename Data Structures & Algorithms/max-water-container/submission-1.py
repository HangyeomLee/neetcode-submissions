class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        lp = 0
        rp = len(heights) - 1
        for i in range(len(heights)):
            if heights[lp] > heights[rp]:
                max_val = max(heights[rp]*(rp-lp),max_val)
                rp = rp - 1
            else:
                max_val = max(heights[lp]*(rp-lp),max_val)
                lp = lp + 1
        return max_val