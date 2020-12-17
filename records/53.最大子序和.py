#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp[i] 表示以nums[i]结尾的最大子序列和
        dp = [nums[i] for i in range(n)]
        # base case
        dp[0] = nums[0]
        # dynamic infer
        for i in range(n):
            # 要么加入前面的序列，要么开始一个新的序列
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


# @lc code=end
