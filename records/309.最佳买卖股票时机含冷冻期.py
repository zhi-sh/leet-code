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
        dp_i0 = 0
        dp_i1 = -float('inf')
        dp_pre_0 = 0
        for i in range(sz):
            tmp = dp_i0
            dp_i0 = max(dp_i0, dp_i1 + prices[i])
            dp_i1 = max(dp_i1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp
        return dp_i0

# @lc code=end
