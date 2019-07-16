"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            res = 1
            while n != 0:
                res *= n
                n -= 1
            return res
        
        helper = range(1, n+1)
        result = []
        a = k - 1
        b = n - 1
        if n == 1:
            return '1'
        while True:
            c = a / factorial(b)
            d = a % factorial(b)
            result.append(helper[c])
            helper.pop(c)
            a, b = d, b - 1
            if b == 0:
                break
        result.append(helper[0])
        return ''.join(str(x) for x in result)