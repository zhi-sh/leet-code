#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = []
        visited = set()
        queue.append(root)
        visited.add(root)
        depth = 1

        while queue:
            sz = len(queue)
            for _ in range(sz):
                elem = queue.pop(0)
                if (elem.left is None) and (elem.right is None):
                    return depth
                if elem.left is not None:
                    queue.append(elem.left)
                if elem.right is not None:
                    queue.append(elem.right)
            depth += 1
        return depth


# @lc code=end
