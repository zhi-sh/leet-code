#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_with(nums[:-1]), self.rob_with(nums[1:]))

    def rob_with(self, nums):
        dp_i = 0
        dp_i_1 = 0
        dp_i_2 = 0
        for i in range(len(nums) - 1, -1, -1):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i


# @lc code=end
