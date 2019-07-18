# coding=utf-8
"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
        	return True
        if not p or not q:
        	return False
        if p.val != q.val:
        	returnn False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)