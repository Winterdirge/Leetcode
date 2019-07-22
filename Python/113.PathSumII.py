# coding=utf-8
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(root, n, path):
            if not root:
                return
            if not root.left and not root.right:
                if n == root.val:
                    res.append(path+[root.val])
                    return
            helper(root.left, n - root.val, path+[root.val])
            helper(root.right, n - root.val, path+[root.val])
        helper(root, sum, [])
        return res