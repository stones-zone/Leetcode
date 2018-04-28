# -*- coding:utf-8 -*-


# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
#
#
# Given an integer n, generate the nth term of the count-and-say sequence.
#
#
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#
# Example 1:
#
# Input: 1
# Output: "1"
#
#
#
# Example 2:
#
# Input: 4
# Output: "1211"
#
#


class Solution(object):
    def get_next(self, seq):
        i, next_seq = 0, ""
        seq =  seq + str(0)
        while i < len(seq) - 1:
            cnt = 1
            while seq[i] == seq[i+1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return str(0)
        seq = "1"
        for i in range(n - 1):
            seq = self.get_next(seq)
        return seq
