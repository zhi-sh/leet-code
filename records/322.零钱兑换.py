#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 记录表中amount+1等价于无穷大
        table = [(amount + 1) for _ in range(amount + 1)]
        table[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                table[i] = min(table[i], 1 + table[i - coin])

        return -1 if table[amount] == (amount + 1) else table[amount]


# @lc code=end
