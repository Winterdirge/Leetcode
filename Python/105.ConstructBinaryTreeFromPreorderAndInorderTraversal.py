# coding=utf-8
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        root = TreeNode(preorder[0])

        root_index_in_inorder = inorder.index(preorder[0])

        
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[1+root_index_in_inorder:]

        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder)]


        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root