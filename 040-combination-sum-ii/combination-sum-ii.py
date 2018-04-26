# -*- coding:utf-8 -*-


# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#
#


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSum2Rec(sorted(candidates), target, 0, [], result)
        return result
    
    def combinationSum2Rec(self, candidates, target, start, tmp, result):
        if target == 0:
            result.append(list(tmp))
        pre = 0
        while start < len(candidates) and candidates[start] <= target:
            # use the second '1' as first round will contain duplicate combinations.
            if pre != candidates[start]:
                tmp.append(candidates[start])
                self.combinationSum2Rec(candidates, target - candidates[start], start + 1, tmp, result)
                tmp.pop()
                pre = candidates[start]
            start += 1
        
