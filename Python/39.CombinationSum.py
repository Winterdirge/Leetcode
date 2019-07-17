# coding=utf-8
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(index, tmp):
            if sum(tmp) == target:
                res.append(tmp[:])
                return
            for i in range(index, len(candidates)):
                if sum(tmp) + candidates[i] > target:
                    break
                tmp.append(candidates[i])
                backtrack(i, tmp)
                tmp.pop()
        res = []
        candidates.sort()
        backtrack(0, [])
        return res
