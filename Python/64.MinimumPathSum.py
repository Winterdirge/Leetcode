"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(1, cols):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        for i in range(1, rows):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]