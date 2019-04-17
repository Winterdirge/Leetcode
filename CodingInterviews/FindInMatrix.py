# 二维数组中的查找
def findInMatrix(matrix, val):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    if not matrix:
        return False
    rows = len(matrix)
    columns = len(matrix[0])
    row = 0
    column = columns - 1
    while column >= 0 and row < rows:
        if matrix[row][column] == val:
            return True
        elif matrix[row][column] > val:
            column -= 1
        else:
            row += 1
    return False