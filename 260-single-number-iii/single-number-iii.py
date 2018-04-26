# -*- coding:utf-8 -*-


#
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
#
# For example:
#
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
#
# Note:
#
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def singleNumber(self, nums):
        axorb =  reduce(operator.xor, nums)
        bit = axorb & -axorb
        a = 0
        for i in nums:
            if i & bit:
                a ^= i
        return [a, a ^ axorb]
    
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = reduce(operator.xor, nums)
        bit = a & -a
        result = [0, 0]
        for i in nums:
            result[bool(i & bit)] ^= i
        return result
        
