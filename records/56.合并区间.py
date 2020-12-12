# @before-stub-for-debug-begin
from python3problem56 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: (e[0], e[1]))

        left = intervals[0][0]
        right = intervals[0][1]

        res = []
        for i in range(1, len(intervals)):
            e = intervals[i]
            if e[0] > right:
                res.append([left, right])
                left = e[0]
                right = e[1]
            if right < e[1]:
                right = e[1]
        res.append([left, right])
        return res


# @lc code=end
