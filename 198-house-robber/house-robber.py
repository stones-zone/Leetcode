# -*- coding:utf-8 -*-


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.


class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            a, b = max(b + num, a), a
        return a
        
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
        
