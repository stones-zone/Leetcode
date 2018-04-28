# -*- coding:utf-8 -*-


# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.
#
#
# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.
#
#
# Example:
#
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
#
# Return 4.
#
#
#
#
#
# The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
#
#
#
#
# After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
#


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        m, n, pq = len(heightMap), len(heightMap[0]), []
        for i, j in zip([0]*n + range(1, m-1)*2 + [m-1]*n, range(n)+[0]*(m-2)+[n-1]*(m-2)+range(n)):
            heapq.heappush(pq, (heightMap[i][j], i, j))
            heightMap[i][j] = -1
        '''
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        '''
        #do dfs
        res = 0
        def dfs(i, j, curr_height, curr_res):
            for next_i, next_j in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0<=next_i<len(heightMap) and 0<=next_j<len(heightMap[0]) and heightMap[next_i][next_j] >= 0:
                    new_height = heightMap[next_i][next_j]
                    heightMap[next_i][next_j] = -1
                    if new_height < curr_height:
                        #we can secure how much water?
                        curr_res += curr_height-new_height
                        #continue to expand
                        curr_res = dfs(next_i, next_j, curr_height, curr_res)   #note the boundary height will not change...
                    else:
                        #the boundary must be changed now
                        heapq.heappush(pq, (new_height, next_i, next_j))
                
            return curr_res
        
        #for all the boundary points...
        while pq:
            curr_height, curr_i, curr_j = heapq.heappop(pq)
            res = dfs(curr_i, curr_j, curr_height, res)
        return res
    
    def trapRainWater1(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in xrange(m)]

        # Push all the block on the border into heap
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        '''
        for i in xrange(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0] = 1
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][n-1] = 1
        for j in xrange(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            visited[0][j] = 1
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[m-1][j] = 1
        '''
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result
        
