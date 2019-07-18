# coding=utf-8
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower=float('-inf'), upper=float('inf')):
        	if not node:
        		return True
        	if node.val <= lower or node.val >= upper:
        		return False
        	if not helper(node.right, node.val, upper):
        		return False
        	if not helper(node.left, lower, node.val):
        		return False
        	return True
        return helper(root)