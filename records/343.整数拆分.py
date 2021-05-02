#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)  
        
        dp[0] = 1
        dp[1] = 1  # i=1
        dp[2] = 1  # i=2 

        for i in range(2, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
            # print(i, dp)
        
        return dp[n]
# @lc code=end

