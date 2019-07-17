# coding=utf-8
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i, res = 0, 0
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i, dic[s[j]])
            res = max(res, j - i + 1)
            dic[s[j]] = j + 1
        return res
