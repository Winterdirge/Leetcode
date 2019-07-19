# coding=utf-8
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        m = len(nums) / 2
        root = TreeNode(nums[m])
        l = nums[:m]
        r = nums[m+1:]
        root.left = self.sortedArrayToBST(l)
        root.right = self.sortedArrayToBST(r)
        return root