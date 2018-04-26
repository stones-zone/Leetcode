# -*- coding:utf-8 -*-


# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
#
# 	Each child must have at least one candy.
# 	Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
# Example 1:
#
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#
#
# Example 2:
#
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.
#
#


import operator
class Solution(object):
    def candy1(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        candies = [1 for _ in range(length)]
        
        for i in range(length - 1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1
        for i in reversed(range(1, length)):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1
        return reduce(operator.add, candies)
    
    def candy(self, ratings):
        def Count(s1, s2):
            if s1 < s2:
                s1, s2 = s2, s1
            return ((s1 + 1) * (s1 + 2) / 2) + (s2 * (s2 + 1) / 2)
        
        if len(ratings) < 2:
            return len(ratings)
        
        rec, dec, count, extra = 0, 0, 0, 0
        for i in range(len(ratings) - 1):
            if ratings[i] <= ratings[i+1]:
                if dec !=0 or ratings[i] == ratings[i+1]:
                    count += Count(rec, dec)
                    rec, dec = 0, 0
                    if ratings[i] < ratings[i+1]:
                        rec += 1
                        extra += 1
                else:
                    rec += 1
            else:
                dec += 1
        count += Count(rec, dec) - extra
        return count
        
        
