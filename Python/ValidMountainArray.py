# 941. Valid Mountain Array
"""
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
"""
class Solution(object):
    def validMoutainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        topIndex = -1
        for i in range(1, len(A)):
            if A[i] == A[i - 1]: # 有相同值直接返回false
                return False
            elif i == 1 and A[i] < A[i - 1]: #开头递减直接返回false
                return False
            elif A[i] < A[i - 1] and topIndex == -1: # 找到峰值
                topIndex = i - 1
            elif A[i] > A[i - 1] and topIndex != -1: # 再次出现峰值返回false
                return False
            elif i == len(A) - 1 and topIndex == -1: # 递增返回false
                return False
        return True
print Solution().validMoutainArray([1,2,3,4,5,4])