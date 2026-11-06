class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        left, right = 0, len(prices) - 1

        while left < len(prices) - 1:
            if right == left:
                right = len(prices) - 1
                left += 1
            profit = prices[right] - prices[left]
            if profit > diff:
                diff = profit
            right -= 1
        return diff