# coding=utf-8
# 766. Toeplitz Matrix
"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right 
has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        res = True
        if len(matrix) == 1:
            return True
        for i in range(1, len(matrix)):
            res &= (matrix[i][1:] == matrix[i-1][0:-1])
        return res
print Solution().isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
])
