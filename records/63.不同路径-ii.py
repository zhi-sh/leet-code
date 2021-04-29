#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        
        for i in range(len(dp)):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1        
        for j in range(len(dp[0])):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1 

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
# @lc code=end

