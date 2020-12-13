#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历
        # 1. 左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        # 2. 将左子树作为右子数
        root.left = None
        root.right = left
        # 3. 将原先的右子数连接到当前的右子树的末端
        p = root
        while p.right is not None:
            p = p.right
        p.right = right


# @lc code=end
