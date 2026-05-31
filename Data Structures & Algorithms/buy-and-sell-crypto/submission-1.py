# Track the lowest price seen so far.
# At each price, calculate the profit if we sell today.
# Update maxProfit with the best profit found.
# This finds the best single buy-sell transaction.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProfit = max(maxProfit, price - minPrice)
        return maxProfit