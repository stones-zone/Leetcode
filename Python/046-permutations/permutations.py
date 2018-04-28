# -*- coding:utf-8 -*-


# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution(object):
    # Backtracking
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [0] * len(nums)
        self.permuteRec(result, nums, [], used)
        return result
    
    def permuteRec(self, result, nums, tmp, used):
        if len(tmp) == len(nums):
            result.append(list(tmp))
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = 1
                tmp.append(nums[i])
                self.permuteRec(result, nums, tmp, used)
                tmp.pop()
                used[i]= 0
    # Insert
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm.append(perm[:i] + [n] + perm[i:])
            perms = new_perm
        return perms
            
            
        
