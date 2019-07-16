"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
"""
def generateMatrix(n):
    l, r, t, b = 0, n-1, 0, n-1
    cur, tar = 1, n*n
    res = [[0 for _ in range(n)] for _ in range(n)]
    while cur <= tar:
        # 从左到右
        for i in range(l, r+1):
            res[t][i] = cur
            cur += 1
        t += 1
        # 从上到下
        for i in range(t, b+1):
            res[i][r] = cur
            cur += 1
        r -= 1
        # 从右到左
        for i in range(r, l-1, -1):
            res[b][i] = cur
            cur += 1
        b -= 1
        # 从下到上
        for i in range(b, t-1, -1):
            res[i][l] = cur
            cur += 1
        l += 1
    return res