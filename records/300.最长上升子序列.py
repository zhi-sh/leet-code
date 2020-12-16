#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] 表示nums[i]这个数结尾的最长子序列
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# @lc code=end
