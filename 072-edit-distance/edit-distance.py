# -*- coding:utf-8 -*-


# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# 	Insert a character
# 	Delete a character
# 	Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#


class Solution(object):
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0 for _ in xrange(l2)] for _ in xrange(l1)]
        for i in xrange(l1):
            dp[i][0] = i
        for j in xrange(l2):
            dp[0][j] = j
        for i in xrange(1, l1):
            for j in xrange(1, l2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]
    
    def minDistance(self, word1, word2):   
        dp = [[-1] * (len(word2)+1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        def edit_dist(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i-1] == word2[j-1]:
                dp[i][j] = edit_dist(i-1, j-1)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(edit_dist(i-1,j-1), edit_dist(i,j-1), edit_dist(i-1,j))
                return dp[i][j]
        return edit_dist(len(word1), len(word2))
