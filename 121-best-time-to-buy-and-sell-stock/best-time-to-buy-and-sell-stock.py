class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        minval = 100001
        maxval = -1
        leftarr = [-1] * len(prices)
        rightarr = [-1] * len(prices)

        for i in range(1, len(prices)):
            minval = min(minval, prices[i-1])
            leftarr[i] = minval
        
        for i in range(len(prices)-1, -1, -1):
            maxval = max(maxval, prices[i])
            rightarr[i] = maxval

        # print(leftarr)
        # print(rightarr)

        for i, p in enumerate(prices):
            if leftarr[i] == -1 or rightarr[i] == -1:
                continue
            else:
                maxprofit = max(maxprofit, rightarr[i]-leftarr[i])

        return maxprofit