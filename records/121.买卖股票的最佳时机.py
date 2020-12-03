#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        dp = [[0] * 2 for _ in range(sz)]
        for i in range(sz):
            if i - 1 == -1:
                dp[i][0] = 0  # dp[i][0] = max(dp[-1][0], d[-1][1]+price[i]) = max(0, -inf+price[i])
                dp[i][1] = -prices[i]  # dp[i][1] = max(dp[i-1][1], dp[i-1][0]-price[i]) = max(-inf, 0-prices[i])
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[sz - 1][0]


# @lc code=end
