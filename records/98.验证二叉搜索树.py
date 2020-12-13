#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkValidBST(root, None, None)

    # 限定root为根的子树节点必须满足hi.val > root.val > lo.val
    def checkValidBST(self, root, lo, hi):
        if root is None:
            return True
        # 若root.val 不符合 max 和 min 限制，则说明不合法
        if lo is not None and root.val <= lo.val:
            return False
        if hi is not None and root.val >= hi.val:
            return False

        # 限定左子树的最大值是root.val, 右子数的最小值是root.val
        return self.checkValidBST(root.left, lo, root) and self.checkValidBST(
            root.right, root, hi)


# @lc code=end
