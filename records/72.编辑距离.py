#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 自顶向下
        # self.memo = {}
        # self.s1 = word1
        # self.s2 = word2
        # return self.top_down(len(word1) - 1, len(word2) - 1)

        # 自底向上
        return self.down_top(word1, word2)

    def top_down(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == -1: return j + 1
        if j == -1: return i + 1

        if self.s1[i] == self.s2[j]:
            return self.top_down(i - 1, j - 1)
        else:
            self.memo[(i, j)] = min(
                self.top_down(i, j - 1) + 1,  # s1 插入
                self.top_down(i - 1, j) + 1,  # s1 删除
                self.top_down(i - 1, j - 1) + 1  # s1 替换
            )
            return self.memo[(i, j)]

    def down_top(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # base case
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                                   dp[i - 1][j - 1] + 1)
        return dp[m][n]


# @lc code=end
