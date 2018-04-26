# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note:
#
#
# 	1 is typically treated as an ugly number.
# 	Input is within the 32-bit signed integer range.
#
#
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
#


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for p in [2, 3, 5]:
            while num % p == 0:
                num = num // p
        return num == 1
