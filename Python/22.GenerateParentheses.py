"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
"""
class Solution(object):
    def generationParenthesis(self, n):
        def backtrack(tmp, l, r):
            if len(tmp) == 2 * n:
                res.append(tmp)
                return
            if l > 0:
                backtrack(tmp+'(', l-1, r)
            if r > l:
                backtrack(tmp+')', l, r-1)
        res = []
        backtrack('', n, n)
        return res