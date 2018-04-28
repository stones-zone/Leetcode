# -*- coding:utf-8 -*-


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#


class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        g_max = c_max = nums[0]
        for i in range(1, len(nums)):
            c_max = max(nums[i], c_max + nums[i])
            g_max = max(g_max, c_max)
        """
            if c_max == nums[i]:
                start = i
            if g_max == c_max:
                end = i
        if len(nums) > 1:
            print nums[start:end+1]
        else:
            print nums[0]
        """
        return g_max
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, s = None, 0
        for num in nums:
            s += num
            if res is None or s > res:
                res = s
            if s < 0:
                s = 0
        return res
