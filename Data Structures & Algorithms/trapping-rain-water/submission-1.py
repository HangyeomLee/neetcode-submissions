class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        lcol = 0
        rcol = 0
        lp = 0
        rp = len(height) - 1
        while lp < rp:
            lcol = max(lcol , height[lp])
            rcol = max(rcol , height[rp])
            if lcol > rcol:
                water += rcol - height[rp]
                rp = rp - 1
            else:
                water += lcol - height[lp]
                lp = lp + 1
        return water
            



