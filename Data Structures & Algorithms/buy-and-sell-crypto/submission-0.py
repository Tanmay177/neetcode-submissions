class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        diff_max = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] > prices[j]:
                    diff = 0
                    continue
                else:
                    diff = prices[j]-prices[i]
                    diff_max = max( diff_max, diff )
        return diff_max
        