#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        # 路径： 记录在track中
        # 选择列表：nums不在track中的元素
        # 结束条件：nums元素全在track中
        self.backtrack(res, track, nums)
        return res

    def backtrack(self, paths, track, nums):
        # 结束条件
        if len(track) == len(nums):
            paths.append(track.copy())
            return

        for i in range(len(nums)):
            # 排除不合法的选择
            if nums[i] in track:
                continue
            # 做选择
            track.append(nums[i])
            # 进入下一层决策树
            self.backtrack(paths, track, nums)
            # 取消选择
            track.pop(-1)


# @lc code=end
