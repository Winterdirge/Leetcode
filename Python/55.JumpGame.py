# coding=utf-8
"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
"""
def canJump(nums):
    tmp = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= tmp:
            tmp = i
    return tmp == 0
