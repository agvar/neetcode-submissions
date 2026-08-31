class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        here we need to find the lowest price seen so far
        then at every new price/index calculate the profit. Now if
        the price at the index is less than lowest, then that price is
        the lowest. If not, then calculate the profit
        """
        left = 0
        right = left + 1
        max_profit = 0

        if len(prices) <= 1:
            return 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit,prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_profit



        