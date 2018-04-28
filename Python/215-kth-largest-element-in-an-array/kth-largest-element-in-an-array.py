# -*- coding:utf-8 -*-


# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
#


from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            pivot_id = randint(left, right)
            new_pivot_id = self.partition_pivot(left, right, pivot_id, nums)
            if new_pivot_id == k - 1:
                return nums[new_pivot_id]
            elif new_pivot_id < k - 1:
                left = new_pivot_id + 1
            else:
                right = new_pivot_id - 1
                
    def partition_pivot(self, left, right, pivot_id, num):
        num[right], num[pivot_id] = num[pivot_id], num[right]
        new_pivot_id = left
        for i in range(left, right):
            if num[i] > num[right]:
                num[i], num[new_pivot_id] = num[new_pivot_id], num[i]
                new_pivot_id += 1
        num[right], num[new_pivot_id] = num[new_pivot_id], num[right]
        return new_pivot_id
            
        
