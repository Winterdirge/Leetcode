# coding=utf-8
# 922. Sort Array By Parity II
"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；
当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。
"""
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1 != 0:
                while A[j] & 1 != 0:
                    j += 2
                    A[i], A[j] = A[j], A[i]
        return A
