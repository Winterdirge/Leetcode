# Given a positive integer num, write a function which returns True
# if nums is a perfect square else False
# Do not use build-in library function such as `sqrt`
# 画出y = x^2 - n的曲线
# 任取一点(k, k^2 - n),经过此点的切线为 y = 2kx - k^2 - n
# 与x轴交点为(1/2*(k + n / k), 0),此点会逼近与y=x^2 - n的根
# 找到该点对应y=x^2-n上的点，在对应点再做切线，又会找到一个与x轴交点，这样经过有限次迭代之后
# 最终会找到方程的根，也就是n的平方根
# 其实上面的方法就是传说中的牛顿迭代法
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        k = num
        while k * k > num:
            k = (k + num / k) / 2
        return k * k == num