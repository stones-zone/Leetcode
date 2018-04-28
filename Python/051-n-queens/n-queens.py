# -*- coding:utf-8 -*-


# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
#
#


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.solutions = []
        self.col = [0] * n
        self.pie = [0] * (2 * n - 1)
        self.na = [0] * (2 * n - 1)
        self.solveNQueensRec([], 0, n)
        return self.solutions
    
    def solveNQueensRec(self, solution, row, n):
        if row == n:
            #self.solutions.append(map(lambda x: '.' * x + 'Q' + '.' * (n - 1 - x), solution))
            self.solutions.append(['.' * x + 'Q' + '.' * (n - 1 - x) for x in solution])
            return
        for i in range(n):
            if not self.col[i] and not self.pie[row + i] and not self.na[row + n - 1 - i]:
                self.col[i] = self.pie[row + i] = self.na[row + n - 1 -i] = 1
                self.solveNQueensRec(solution + [i], row + 1, n)
                self.col[i] = self.pie[row + i] = self.na [row + n -1 -i] = 0
    '''
    def toList(self, state):
        n = len(state)
        """
        result = []
        for i in range(n):
            t = state[i]
            temp = "."*t + "Q" + "."*(n-t-1)
            result.append(temp)
        return result
        """
        return ["."*x+"Q"+"."*(n-x-1) for x in state]
        
    def DFS(self, result, state, index, col_mark, back_dia_mark, forw_dia_mark):
        """
        find all solutions of NQueens problem
        
        :type result: List[List[str]]
        :type index: int
        :rtype: None
        """
        n = len(state)
        
        if (index == n):
            result.append(self.toList(state))
        else:
            for i in range(n):
                if (col_mark[i] and back_dia_mark[index+i] and forw_dia_mark[index-i+n-1]):
                    col_mark[i] = False
                    back_dia_mark[index+i] = False
                    forw_dia_mark[index-i+n-1] = False
                    state[index] = i
                    self.DFS(result, state, index+1, col_mark, back_dia_mark, forw_dia_mark)
                    state[index] = -1
                    forw_dia_mark[index-i+n-1] = True
                    back_dia_mark[index+i] = True
                    col_mark[i] = True
        
    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        state = [-1]*n
        index = 0
        col_mark = [True]*n
        back_dia_mark = [True]*(2*n-1)
        forw_dia_mark = [True]*(2*n-1)
        self.DFS(result, state, index, col_mark, back_dia_mark, forw_dia_mark)
        return result
    '''
