# coding=utf-8
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root,]
        level = 0
        while queue:
            tmp = []
            tmp_queue = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            if level % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp[:])
            level += 1
            queue = tmp_queue
        return res