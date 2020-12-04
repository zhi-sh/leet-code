#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        ks = k + 1
        sz = len(prices)
        dp = [[[0] * 2 for _ in range(ks)] for i in range(sz)]
        for i in range(sz):
            for j in range(ks - 1, 0, -1):
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[sz - 1][k][0]

# @lc code=end
