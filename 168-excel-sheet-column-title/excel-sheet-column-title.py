# -*- coding:utf-8 -*-


# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
#


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n:
            result += chr((n - 1) % 26 + ord('A'))
            n = (n - 1) / 26
        return result[::-1]
        
