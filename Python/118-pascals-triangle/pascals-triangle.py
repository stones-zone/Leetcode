# -*- coding:utf-8 -*-


# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i): #i
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j] #j
        return res
    
    def generate1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(numRows - 1):
            res.append(list(map(lambda x, y: x + y, [0] + res[-1], res[-1] + [0])))
        return res
    
    
        
