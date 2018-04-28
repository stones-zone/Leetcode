# -*- coding:utf-8 -*-


# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#


class Solution(object):
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j -1
        return True
    
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sn = s.encode('utf-8').translate(None, string.punctuation + ' ').lower()
        return sn == sn[::-1]
        
