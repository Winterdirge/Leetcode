# coding=utf-8
"""
给定一个二叉树，检查它是否是镜像对称的。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(p, q):
        	if p is None and q is None:
        		return True
        	if p is None or q is None:
        		return False
        	return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
        return helper(root, root)