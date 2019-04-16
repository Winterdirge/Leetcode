# coding=utf-8
# 696. Count Binary Substrings
"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，
并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :param s: str
        :return: int
        """
        last, cur, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                last = cur
                cur = 1
            if last >= cur:
                res += 1
        return res

print Solution().countBinarySubstrings("00110")
