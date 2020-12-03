#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_k_0 = 0  # 初始仓位
        dp_i_k_1 = -float('inf')
        for i in range(len(prices)):
            tmp = dp_i_k_0
            dp_i_k_0 = max(dp_i_k_0, dp_i_k_1 + prices[i])
            dp_i_k_1 = max(dp_i_k_1, tmp - prices[i])
        return dp_i_k_0


# @lc code=end
