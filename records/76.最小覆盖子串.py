# @before-stub-for-debug-begin
from python3problem76 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 初始化need
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        left = right = 0  # [left, right)
        valid = 0  #窗口中满足 need 条件的字符个数，如果 valid 和 need.size 的大小相同，则说明窗口已满足条件，已经完全覆盖了串 T。
        start, length = 0, len(s) + 1

        while right < len(s):
            c = s[right]  # 将移入窗口的字符
            right += 1  # 右移窗口

            # 进行窗口内数据更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否需要收缩
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]  # 将要移除窗口的字符
                left += 1  # 引动左边界

                # 进行窗口内数据更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return '' if length == len(s) + 1 else s[start:start + length]


# @lc code=end
