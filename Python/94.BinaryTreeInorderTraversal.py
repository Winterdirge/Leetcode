# coding=utf-8
# 给定一个二叉树，返回它的中序遍历。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        cur = root
        stack = []
        res = []
        while cur or stack:
        	while cur:
        		stack.append(cur)
        		cur = cur.left
        	cur = stack.pop()
        	res.append(cur.val)
        	cur = cur.right