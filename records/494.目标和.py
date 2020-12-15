#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # --------- 回溯法
        # self.result = 0
        # if len(nums) == 0:
        #     return 0
        # self.backtrack(nums, 0, S)
        # return self.result

        # --------- 子集划分
        # sum(a) - sum(b) = target
        # sum(a) = target + sum(b)
        # sum(a) + sum(a) = target + sum(b) + sum(a)
        # sum(a) = (target + sum(nums))/2
        SUMS = sum(nums) + S
        if SUMS % 2 != 0 or sum(nums) < S:
            return 0
        sums = SUMS // 2

        return self.subsets(nums, sums)

    def subsets(self, nums, sums):
        n = len(nums)
        # dp[i][j] i个物品时，j的容量能否装下
        dp = [[0 for j in range(sums + 1)] for i in range(n + 1)]
        for i in range(len(dp)):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(sums + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][sums]

    def backtrack(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                self.result += 1
            return

        # 选择+
        rest -= nums[i]
        self.backtrack(nums, i + 1, rest)
        rest += nums[i]  # 撤销选择

        # 选择-
        rest += nums[i]
        self.backtrack(nums, i + 1, rest)
        rest -= nums[i]  # 撤销选择


# @lc code=end
