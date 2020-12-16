#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        nums = [e[1] for e in envelopes]
        return self.lengthOfLIS(nums)

    def lengthOfLIS(self, nums):
        n = len(nums)

        # dp[i] 表示nums[i]这个数结尾的最长子序列
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# @lc code=end
