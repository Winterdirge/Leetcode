# coding=utf-8
# 884. 两句话中的不常见单词
"""
给定两个句子A和B（句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，
那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。
"""
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # 本来还想着用两个字典，后来发现一个就够了
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        return [word for word in count if count[word] == 1]

