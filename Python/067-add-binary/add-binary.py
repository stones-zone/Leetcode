# -*- coding:utf-8 -*-


# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#


class Solution(object):
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        carry, result = 0, ""
        length = max(len(a), len(b))
        for i in range(length):
            remd = carry
            if i < len(a):
                remd += int(a[-i-1])
            if i < len(b):
                remd += int(b[-i-1])
            carry, remd = remd // 2, remd % 2
            result += str(remd)
        if carry:
            result += str(carry)
        return result[::-1]
                
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]  
