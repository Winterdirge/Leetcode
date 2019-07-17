# coding=utf-8
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 简单的排列组合问题
        # 从m+n-2步中选n-1步向下即可
        a = 1
        b = 1
        for i in range(m - 1):
            a *= m + n - 2 - i
            b *= i + 1
        return a / b
