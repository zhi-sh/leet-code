#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        sz = len(nums)
        wt = total // 2 + 1
        dp = [False for _ in range(wt)]
        dp[0] = True
        for i in range(sz):
            for j in range(wt - 1, -1, -1):
                if (j - nums[i] >= 0):
                    dp[j] = dp[j] | dp[j - nums[i]]

        return dp[wt - 1]


# @lc code=end
