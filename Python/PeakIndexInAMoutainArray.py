# coding=utf-8
# 852. Peak Index in a Mountain Array
"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain,
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # mid = l + (r - l) / 2
        # if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
        #     return A[mid]
        # elif A[mid] < A[mid + 1]:
        #     helper(A, mid + 1, r)
        # else:
        #     helper(A, l, mid - 1)
        l, r = 0, len(A) - 1
        while l < r:
            mid = l + (r - l) / 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def peakIndexInMountainArray1(self, A):
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i
