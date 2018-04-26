# -*- coding:utf-8 -*-


# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#
# 	Only one letter can be changed at a time.
# 	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
#
# Note:
#
#
# 	Return 0 if there is no such transformation sequence.
# 	All words have the same length.
# 	All words contain only lowercase alphabetic characters.
# 	You may assume no duplicates in the word list.
# 	You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#
#
#
#


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        forward, backward, r = {beginWord}, {endWord}, 2
        dic = set(string.ascii_lowercase)
        if endWord not in wordList:return 0
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            next = set()
            for word in forward:
                for i, char in enumerate(word):
                    first, second = word[:i], word[i + 1:]
                    for item in dic:
                        candidate = first + item + second
                        if candidate in backward:
                            return r

                        if candidate in wordList:
                            wordList.discard(candidate)
                            next.add(candidate)
            forward = next
            r += 1
        return 0
    
    def ladderLength1(self, beginWord, endWord, wordList):
        distance, cur, lookup = 0, [beginWord], set(wordList)
        if endWord not in wordList: return 0
        while cur:
            next_queue = []

            for word in cur:
                if word == endWord:
                    return distance + 1
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate in lookup:
                            next_queue.append(candidate)
                            lookup.discard(candidate)
            distance += 1
            cur = next_queue

        return 0 
