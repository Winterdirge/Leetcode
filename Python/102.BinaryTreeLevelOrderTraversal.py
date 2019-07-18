# coding=utf-8
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    # 递归
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        
        levels = []
        if not root:
            return []
        helper(root, 0)
        return levels
    # 迭代
    def levelOrder2(self, root):
        levels = []
        if not root:
            return levels
        level = 0
        queue = [root]
        while queue:
            levels.append([])
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.pop(0)
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return levels