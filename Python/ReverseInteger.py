# coding=utf-8
#7 整数反转
"""
注意:
假设我们的环境只能存储得下 32 位的有符号整数，
则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，
如果反转后整数溢出那么就返回 0。
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while x != 0:
            remain = x % 10
            x /= 10
            if res > (2**31-1) // 10 or (res == 2**31-1 and remain > 7):
                return 0
            
            #此处有问题，python负数是向下取整
            if res < (-2**31) // 10 or (res == -2**31 and remain < -8):
                return 0
            res = res * 10 + remain
        return res
