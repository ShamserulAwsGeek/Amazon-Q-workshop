from typing import List
from typing import List
from typing import List
#You are given an array prices where prices[i] is the price of a given stock on the i^th^ day.
#Find the maximum profit you can achieve. You may complete at most two transactions.
#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
  #Example 1:
#Input: prices = [3,3,5,0,0,3,1,4]
#Output: 6
#Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
#Example 2:
#Input: prices = [1,2,3,4,5]
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
#Example 3:
#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.
#Example 4:
#Input: prices = [1]
#Output: 0
#Constraints:
#1 <= prices.length <= 105
#0 <= prices[i] <= 105
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        left = [0] * n
        right = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_price)
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i + 1], max_price - prices[i])
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left[i] + right[i])
        return max_profit


#Another suggestion:

import List

class Solution: 
    def maxProfit(self, prices: List[int]) -> int: 
    if not prices:
        return 0

        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = 2
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = float('-inf')
            for d in range(1, n):
                max_diff = max(max_diff, dp[t - 1][d - 1] - prices[d - 1])
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)

        return dp[k][-1]

def test_max_profit():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([3,3,5,0,0,3,1,4], 6),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
        ([1], 0),
        ([], 0)
    ]
    
    for prices, expected in test_cases:
        result = solution.maxProfit(prices)
        print(f"Prices: {prices}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 40)

# Run tests
test_max_profit()
