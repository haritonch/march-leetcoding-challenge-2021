class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = 0, float('-inf')
        for price in prices:
            buy = max(buy, sell + price - fee)
            sell = max(sell, buy - price)
        return buy
