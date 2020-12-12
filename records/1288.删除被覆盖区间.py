#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#


# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda e: (e[0], -e[1]))
        # 记录合并区的起点和终点
        left = intervals[0][0]
        right = intervals[0][1]

        res = 0
        for i in range(1, len(intervals)):
            intv = intervals[i]
            # 1. 找到覆盖区间
            if left <= intv[0] and right >= intv[1]:
                res += 1

            # 2. 找到相交区间，合并
            if right >= intv[0] and right <= intv[1]:
                right = intv[1]

            # 3. 完全不想交， 更新起点和终点
            if right < intv[0]:
                left = intv[0]
                right = intv[1]
        return len(intervals) - res


# @lc code=end
