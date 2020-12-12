#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        tuples = self.nSumTarget(nums, 4, 0, target)
        return tuples

    def nSumTarget(self, nums, n, start, target):
        res = []
        sz = len(nums)
        if n < 2 or sz < n:
            return res
        if n == 2:  # TwoSum is base case
            lo, hi = start, sz - 1
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
        else:
            prev = float('inf')
            for i in range(start, sz):
                if prev == nums[i]:
                    continue
                else:
                    prev = nums[i]

                tuples = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in tuples:
                    arr.append(nums[i])
                    res.append(arr)
        return res


# @lc code=end
