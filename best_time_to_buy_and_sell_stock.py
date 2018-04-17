# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# In this case, no transaction is done, i.e. max profit = 0.

# result: Your runtime beats 98.44 % of python3 submissions
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0;

        if prices[1] - prices[0] > 0:
            max_profit = prices[1] - prices[0]
        else:
            max_profit = 0

        min_elem = prices[0]

        for p in prices[1:]: # already taken care of prices[0]
            if (p - min_elem) > max_profit:
                max_profit = p - min_elem

            if p < min_elem:
                min_elem = p # update min element. max_profit still stays the same

        return max_profit
