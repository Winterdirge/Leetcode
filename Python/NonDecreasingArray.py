# coding=utf-8
"""
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，
该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，
满足 array[i] <= array[i + 1]。

示例 1:
输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:
输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明: n的范围为[1, 10,000]。
"""
# 数组长度小于等于2，一定可以变为升序
# 当出现降序时，当前数字小于上一个数字，这时需要分两种情况
# 1.如果当前数字大于上上个数字（eg:[-1,4,2,3]），这时我们需要修改上一个数字为当前数字
# 2.如果当前数字小于上上个数字（eg:[2,3,3,2,4]），这时需要修改当前数为上一个数字
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        changeCount = 0
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            changeCount += 1
        for i in range(1, len(nums) - 1):
            right = nums[i + 1]
            if right < nums[i]:
                changeCount += 1
                if changeCount > 1:
                    return False
                left = nums[i - 1]
                if left > right:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = left
        return True
