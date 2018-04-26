# -*- coding:utf-8 -*-


# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution(object):
    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = [1]
        # Note: start form 0 or 1
        for i in xrange(rowIndex):
            a = list(map(lambda x, y: x + y, [0] + a, a + [0]))
        return a
        
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """        
        row = [1]
        for l in range(rowIndex):
            row = [1] + [i + j for i, j in zip(row[:-1], row[1:])] + [1]
        return row
