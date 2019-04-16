# coding=utf-8
# 83. Remove Duplicates from Sorted List
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
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
        if not head or not head.next:
            return head
        pre = cur = head
        while head.next:
            if head.next.val != pre.val:
                head = head.next
                pre.next = head
                pre = head
            else:
                head = head.next

        pre.next = head.next

        return cur
    def deleteDuplicates1(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


