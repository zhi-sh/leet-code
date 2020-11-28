#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        window = {}
        left = right = 0
        valid = 0
        start, length = 0, len(s2) + 1
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s2[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return (length == len(s1)) and (set(s2[start:start + length]) == set(s1))


# @lc code=end
