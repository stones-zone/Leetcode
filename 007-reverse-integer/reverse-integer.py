# -*- coding:utf-8 -*-


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) > (2 ** 31):
            print ("input overflow!")
            return 0
        s = (x > 0) - (x < 0)
        r = int(repr(s * x)[::-1])
        return s * r * (r < 2 ** 31)
    
    def reverse1(self, x):
        maxInt = 2**31-1
        minInt = -1 * 2**31
        if x < 0:
            y  = -1 * int(str(-x)[::-1])
        else:
            y  = int(str(x)[::-1])
        if y > maxInt or y < minInt:
            return 0
        return y 
