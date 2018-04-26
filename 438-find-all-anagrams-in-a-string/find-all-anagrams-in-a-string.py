# -*- coding:utf-8 -*-


# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#


class Solution(object):
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        cnt = [0] * 26
        for c in p:
            cnt[ord(c) - ord('a')] += 1
        left, right, result = 0, 0, []
        while right < len(s):
            cnt[ord(s[right]) - ord('a')] -= 1
            while cnt[ord(s[right]) - ord('a')] < 0:
                cnt[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1
        return result
    
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n,m = len (s), len(p)
        target = sorted(p)
        chars = set(p)
        
        result = []
        idx=0
        while idx + m <= n:
            if s[idx] in chars:
                if sorted(s[idx:idx+m])==target:
                    result.append(idx)
                    while idx+m<n:
                        if s[idx]==s[idx+m]:
                            idx+=1
                            result.append(idx)
                        elif s[idx+m] in chars:
                            step = s[idx:idx+m].index(s[idx+m])
                            idx+=step
                            break
                        else:
                            idx+=m
                            break
            idx+=1            
        return result
