#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        sz = len(prices)
        ks = min(1000, len(prices) // 2 + 1)
        dp = [[[0] * 2 for j in range(ks)] for i in range(sz)]
        for i in range(sz):
            for k in range(ks - 1, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1],
                                  dp[i - 2][k - 1][0] - prices[i])
        return dp[sz - 1][ks - 1][0]


# @lc code=end
