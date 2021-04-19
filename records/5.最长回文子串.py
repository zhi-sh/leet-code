#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        dp = [[False]*sz for _ in range(sz)]

        for i in range(sz):
            dp[i][i] = True

        left = right = 0
        for i in range(sz-1, -1, -1):
            for j in range(i+1, sz):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = True and dp[i+1][j-1]
        
                if dp[i][j] and (right - left <= j - i):
                    left = i 
                    right = j
        return s[left:right+1]
# @lc code=end

