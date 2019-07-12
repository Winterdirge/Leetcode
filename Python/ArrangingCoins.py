# coding=utf-8
# 441. Arranging Coins
"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.
示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        tmpSum = 0
        k = 0
        while tmpSum <= n:
            k += 1
            tmpSum += k
        return k - 1

    def arrangeCoins1(self, n):
        # (1+k)*k/2 前k项和 >= n
        # 得出比这个根小的最大整数即可
        # k^2 + k - 2n = 0
        return int(round((-1 + (1 + 8 * n) ** 0.5) / 2))
