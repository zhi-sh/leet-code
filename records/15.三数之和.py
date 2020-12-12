#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0

        nums.sort()
        n = len(nums)
        res = []
        before = float('inf')
        for i in range(n):  # 确保第一个数字，不重复
            if before == nums[i]:
                continue
            else:
                before = nums[i]
            
            tuples = self.twoSum(nums, i + 1, target - nums[i])

            for arr in tuples:
                arr.append(nums[i])
                res.append(arr)
        return res

    def twoSum(self, nums, start, target):
        res = []
        lo, hi = start, len(nums) - 1
        while lo < hi:
            sums = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sums < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sums > target:
                while hi > lo and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while hi > lo and nums[hi] == right:
                    hi -= 1
        return res


# @lc code=end
