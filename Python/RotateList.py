# coding=utf-8
# 61. Rotate List
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        if not head or not head.next:
            return head

        node = head
        length = 1

        # 计算链表长度
        while head.next:
            length += 1
            head = head.next
        # 构造环形链表
        head.next = node
        pre = head

        step = length - k % length  #相当于向右走n-k步
        while step > 0:
            node = node.next
            pre = pre.next
            step -= 1
        pre.next = None
        return node
