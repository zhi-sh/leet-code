#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        sz = len(s)
        dp = [[False] * sz for _ in range(sz)]

        result = 0
        for i in range(sz-1, -1, -1):
            for j in range(i, sz):
                if s[i] == s[j]:
                    if j-i<=1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = True and dp[i+1][j-1]
                if dp[i][j]:
                    result += 1

        return result                             
        
# @lc code=end

