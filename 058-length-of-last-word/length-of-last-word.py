# -*- coding:utf-8 -*-


# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
#
#


class Solution(object):
    def lengthOfLastWord1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, i = 0, len(s) - 1
        if len(s) == 0:
            return length
        while s[i] == " " and i != 0:
            i -= 1
        while i >= 0 and s[i].isalpha():
            length += 1
            i -= 1
        return length
    
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
        
