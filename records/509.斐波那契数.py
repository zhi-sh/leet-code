#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#


# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N <= 0:
            return 0
        if N == 1 or N == 2:
            return 1
        prev = curr = 1
        for i in range(3, N + 1):
            res = prev + curr
            prev = curr
            curr = res
        return curr


# @lc code=end
