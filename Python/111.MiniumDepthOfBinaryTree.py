# coding=utf-8
"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.left or not root.right:
            return l+r+1
        else:
            return min(l,r)+1
    
    def minDepth1(self, root):
        if not root:
            return 0
        stack = [(1, root)]
        while stack:
            n_height, node = stack.pop(0)
            if node:
                if not node.left and not node.right:
                    return n_height
                stack.append((n_height + 1, node.left))
                stack.append((n_height + 1, node.right))
        return height