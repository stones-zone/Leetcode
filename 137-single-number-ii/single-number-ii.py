# -*- coding:utf-8 -*-


# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#


class Solution(object):
    def singleNumber(self, nums):
        a = set(nums);
        a = sum(a) * 3 - sum(nums);
        a = a/2;
        return a;
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for i in nums:
            one = (one ^ i) & ~two
            two = (two ^ i) & ~one
        return one
