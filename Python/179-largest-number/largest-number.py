# -*- coding:utf-8 -*-


# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: 210
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: 9534330
#
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = map(str,nums)
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(nums).lstrip('0') or '0'
