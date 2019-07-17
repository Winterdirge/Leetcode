# coding=utf-8
"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        left, right = None, None
        while p.next:
            left = p.next
            right = left
            while right.next and right.next.val == left.val:
                right = right.next
            if left == right:
                p = p.next
            else:
                p.next = right.next
        return dummy.next