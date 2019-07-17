# coding=utf-8
"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        head1 = dummy1 = ListNode(0)
        head2 = dummy2 = ListNode(0)
        while head:
            if head.val < x:
                dummy1.next = head
                dummy1 = dummy1.next
            else:
                dummy2.next = head
                dummy2 = dummy2.next
            head = head.next
        dummy2.next = None
        dummy1.next = head2.next
        return head1.next