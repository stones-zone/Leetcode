# -*- coding:utf-8 -*-


# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        str_len = len(s)
        
        if str_len <= 1:
            return str_len
        
        if str_len == 2:
            return 1 if s[0] == s[1] else 2
        
        longest = 0
        offset = 0
        index = {}
        
        n = 0
        for ch in s:
            if ch in index and index[ch] >= offset:
                length = n - offset
                if length > longest:
                    longest = length
                offset = index[ch] + 1
            index[ch] = n
            n += 1
            
        length = n - offset
        if length > longest:
            longest = length

        return longest
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest
