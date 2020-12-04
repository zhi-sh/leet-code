# @before-stub-for-debug-begin
# from python3problem123 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        ks = 3
        dp = [[[0] * 2 for _ in range(ks)] for i in range(sz)]
        for i in range(sz):
            for k in range(ks - 1, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[sz - 1][2][0]


# @lc code=end