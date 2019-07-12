# coding=utf-8
# 475. Heaters
"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:
给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
"""
# class Solution(object):
#     def findRadius(self, houses, heaters):
#         """
#         :type houses: List[int]
#         :type heaters: List[int]
#         :rtype: int
#         """

#         def lowerBound(heaters, val):
#             for i in range(len(heaters)):
#                 if heaters[i] > val:
#                     return [val] + heaters[i:]
#                 elif heaters[i] == val:
#                     return heaters[i:]
#             return []



#         if len(heaters) == 1:
#             if heaters[0] <= houses[0]:
#                 return houses[-1] - heaters[0]
#             elif heaters[0] >= houses[-1]:
#                 return heaters[0] - houses[0]
#             else:
#                 return max(heaters[0] - houses[0], houses[-1] - heaters[0])


#         # 五种情况讨论一下
#         if heaters[-1] <= houses[0]:
#             return houses[-1] - heaters[-1]
#         elif heaters[0] < houses[0] < heaters[-1] < houses[-1]:
#             pass
#         elif heaters[0] < houses[0] and heaters[-1] > houses[-1]:
#             pass
#         elif houses[0] < heaters[0] < houses[-1] < heaters[-1]:
#             pass
#         else:
#             return heaters[0] - houses[0]
