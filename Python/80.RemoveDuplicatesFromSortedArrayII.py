# coding=utf-8
"""给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i,j=1,2
        while j < len(nums):
            if nums[j] != nums[i-1]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1