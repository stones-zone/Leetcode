# -*- coding:utf-8 -*-


# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#


class Solution(object):
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(lambda x, y: x >= y, nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.binarySearch(lambda x, y: x > y, nums, target)
        return [left, right - 1]
    def binarySearch(self, compare, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x > A[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x >= A[mid]: left = mid + 1
                else: right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
