class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        lp = 0
        rp = len(heights) - 1
        for i in range(len(heights)):
            max_val = max(min(heights[lp],heights[rp])*(rp-lp),max_val)
            if heights[lp] > heights[rp]:
                rp = rp - 1
            else:
                lp = lp + 1
        return max_val