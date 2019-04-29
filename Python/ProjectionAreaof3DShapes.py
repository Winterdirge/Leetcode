# 883. Projection Area of 3D Shapes
"""
在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
投影就像影子，将三维形体映射到一个二维平面上。
在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。
返回所有三个投影的总面积。
"""
class Solution(object):
    def projectionArea(self, grid):
        # 俯视图直接所有元素个数
        lookDown = sum([len(row) for row in grid])
        # 左边视图找出x相同的元素最大值
        lookLeft = sum([max(grid[i][j] for j in len(grid[i]) for i in len(grid))])
        # 右边找出y相同元素最大值
        lookRight = sum([max(grid[j][i] for j in len(grid[i]) for i in len(grid))])
        return lookDown + lookLeft + lookRight