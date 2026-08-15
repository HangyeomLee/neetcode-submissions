class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r)//2
            count = 0
            for pile in piles:
                count += pile // mid
                if pile % mid != 0:
                    count += 1
            if count <= h:
                r = mid
            elif count > h:
                l = mid + 1
        return l