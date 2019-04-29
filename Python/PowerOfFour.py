# 给定一个整数 (32 位有符号整数)，
# 请编写一个函数来判断它是否是 4 的幂次方。
class Solution(object):
    def isPowerOfFour(self, num):
        # 先检查是不是2的次幂
        if num <= 0 or num & (num-1):
            return False
        # 检查奇数位上的1 0x5=0101b
        return num & 0x55555555