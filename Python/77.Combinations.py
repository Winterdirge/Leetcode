# coding=utf-8
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""
# 回溯法
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(tmp, index):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(index, n+1):
                tmp.append(i)
                backtrack(tmp, i+1)
                tmp.pop()
        res = []
        backtrack([],1)
        return res