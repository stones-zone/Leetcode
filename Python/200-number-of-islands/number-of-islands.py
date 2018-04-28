# -*- coding:utf-8 -*-


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
#


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid[0])
        n = len(grid)
        def sink (x, y):
            if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                grid[x][y] = '0'
                map(sink, [x-1, x+1, x, x], [y, y, y-1, y+1])
                return 1
            return 0
        return sum(sink(x, y) for x in xrange(n) for y in xrange(m))
