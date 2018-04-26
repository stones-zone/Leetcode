# -*- coding:utf-8 -*-


# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#


class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
        
    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [ ]
        i, count = 0, 1 << len(nums)
        while i < count:
            cur = [ ]
            for j in range(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            result.append(cur)
            i += 1
        return result
        
