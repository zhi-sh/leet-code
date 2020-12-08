#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums) + 2)]
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]


# @lc code=end
