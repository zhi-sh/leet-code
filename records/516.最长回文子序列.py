#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def pprint(self, dp):
        for r in dp:
            print(r)
        print('-' * 20)
    
    def longestPalindromeSubseq(self, s: str) -> int:

        sz = len(s)
        dp = [[0]*sz for _ in range(sz)]        

        # init
        for i in range(sz):
            dp[i][i] = 1
        
        for i in range(sz-1, -1, -1):
            for j in range(i+1, sz):
                if s[i] ==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # self.pprint(dp)
        return dp[0][-1]

# @lc code=end

