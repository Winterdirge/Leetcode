# coding=utf-8
# 给定一个矩阵 A， 返回 A 的转置矩阵。
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return None
        result = []
        for j in range(len(A[0])):
            temp = []
            for i in range(len(A)):
                temp.append(A[i][j])
            result.append(temp)
        return result

    def transpose1(self, A):
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
print Solution().transpose1([[1,2,3],[4,5,6],[7,8,9]])
