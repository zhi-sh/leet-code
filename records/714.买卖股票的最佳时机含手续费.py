#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        sz = len(prices)
        for i in range(sz):
            if i - 1 == -1:
                dp_ik0 = 0
                dp_ik1 = -prices[i] - fee
                continue
            tmp = dp_ik0
            dp_ik0 = max(dp_ik0, dp_ik1 + prices[i])
            dp_ik1 = max(dp_ik1, tmp - prices[i] - fee)
        return dp_ik0


# @lc code=end
