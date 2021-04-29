#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sz = len(cost)
        dp = [1e9]*(sz)

        dp[0] = cost[0] # 第1阶
        dp[1] = cost[1]# 第2阶

        for i in range(2, sz):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[sz-1], dp[sz-2])
# @lc code=end

