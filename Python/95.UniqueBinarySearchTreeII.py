# coding=utf-8
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(begin, end):
        	res = []
        	if begin > end:
        		res.append(None)
        		return res
        	for i in range(begin, end + 1):
        		lefts = helper(begin, i - 1)
        		rights = helper(i + 1, end)
        		for l in lefts:
        			for r in rights:
        				root = TreeNode(i)
        				root.left = l
        				root.right = r
        				res.append(root)
        	return res
        return helper(1, n) if n else []