# coding=utf-8
# 107. 二叉树的层次遍历 II
"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        stack = [root]
        res = []
        while len(stack) > 0:
            temp = []
            for i in range(len(stack)):
                node = stack.pop()
                if node:
                    temp.append(node.val)   # 以层层遍历，然后反转就行
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            res.append(temp)  # 或者直接把temp插入第一位就行 res.insert(0, temp)
        return res[::-1]
