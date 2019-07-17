# coding=utf-8
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        visit = [[0 for _ in range(cols)] for _ in range(rows)]

        def backtrack(row, col, i):
            if i == len(word):
                return True
            elif row < 0 or row >= rows or col < 0 or col >= cols or visit[row][col] == 1 or board[row][col] != word[i]:
                return False
            else:
                visit[row][col] = 1
                res = backtrack(row + 1, col, i + 1) or backtrack(row - 1, col, i + 1) or backtrack(row, col + 1, i + 1) or backtrack(row, col - 1, i + 1)
                if res:
                    return True
                else:
                    visit[row][col] = 0
                    return False
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
