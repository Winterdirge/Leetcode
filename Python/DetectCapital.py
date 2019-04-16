# coding=utf-8
"""
502 Detect Capital
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。
示例 1:
输入: "USA"
输出: True
示例 2:
输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 全大写，正确
        if word.upper() == word:
            return True
        firstCapital = False  #第一个字母是否大写
        middleCapital = False #中间是否有大写
        for i in range(len(word)):
            if i == 0 and 'A' <= word[i] <= 'Z':
                firstCapital = True
            elif 'A' <= word[i] <= 'Z':
                middleCapital = True
                break
        if firstCapital and not middleCapital:
            return True
        elif not firstCapital and not middleCapital:
            return True
        return False
print Solution().detectCapitalUse("USA")
print Solution().detectCapitalUse("FlaG")
print Solution().detectCapitalUse("fdsGsd")
