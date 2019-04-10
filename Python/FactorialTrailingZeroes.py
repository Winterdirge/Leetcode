# 转化为求阶乘中5的个数
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n // 5 > 0:
            res += (n // 5)
            n = n // 5
        return res