class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_local = 101 
        max_local = 0
        max_price = 0
        for price in prices:
            min_local = min(min_local, price)
            max_price = max(max_price, price - min_local)
        return max_price