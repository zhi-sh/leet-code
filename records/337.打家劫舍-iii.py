#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.dp(root)
        return max(res[0], res[1])

    # res[0] 不抢root的收益
    # res[1] 抢root的收益
    def dp(self, root):
        if root is None:
            return [0, 0]

        left = self.dp(root.left)
        right = self.dp(root.right)

        # 抢
        rob = root.val + left[0] + right[0]
        # 不抢, 下家可抢可不抢
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return [not_rob, rob]

    # def rob(self, root: TreeNode) -> int:
    #     memo = {}
    #     if root is None:
    #         return 0
    #     if root in memo:
    #         return memo.get(root)

    #     # 抢它
    #     do_it = root.val + (0 if root.left is None else self.rob(
    #         root.left.left) + self.rob(root.left.right)) + (
    #             0 if root.right is None else self.rob(root.right.left) +
    #             self.rob(root.right.right))
    #     # 不抢它
    #     not_do_it = self.rob(root.left) + self.rob(root.right)
    #     res = max(do_it, not_do_it)
    #     memo[root] = res
    #     return res


# @lc code=end
