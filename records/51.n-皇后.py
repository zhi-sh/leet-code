#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        from copy import deepcopy
        self.res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        res = []
        for row in self.res:
            item = []
            for col in row:
                item.append(''.join(col))
            res.append(item)
        return res

    def backtrack(self, board, row):
        if row == len(board):
            self.res.append(deepcopy(board))
            return

        size = len(board[row])
        for col in range(size):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'

    def is_valid(self, board, row, col):
        n = len(board)

        # 检测列是否有皇后冲突
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # 检测右上方
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
            if board[i][j] == 'Q':
                return False

        # 检测左上方
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True


# @lc code=end
