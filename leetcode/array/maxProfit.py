# Best Time to Buy and Sell Stock
## Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # special condition: we need to BUY before we can SELL
        buy = 0 # buy
        sell = 1 # sell
        max_profit = 0

        while sell < len(prices):
            cur_profit = prices[sell] - prices[buy] # track our current profit
            if prices[buy] < prices[sell]:
                max_profit = max(cur_profit, max_profit)
            else:
                buy = sell

            sell += 1

        return max_profit
