class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        minval = 100001

        for p in prices:
            minval = min(minval, p)
            maxprofit = max(maxprofit, p-minval)
        
        return maxprofit