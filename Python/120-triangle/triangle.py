# -*- coding:utf-8 -*-


# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#


class Solution(object):
    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        elif len(triangle) == 1:
            return min(triangle[-1])
        below = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            curr = triangle[i]
            for j in range(len(curr)):
                curr[j] += min(below[j], below[j + 1])
            below = curr
        return curr[0]
