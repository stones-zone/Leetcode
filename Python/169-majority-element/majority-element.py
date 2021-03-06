# -*- coding:utf-8 -*-


# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#


import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]
        
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key = lambda a: a[1], reverse = True)[0][0]
