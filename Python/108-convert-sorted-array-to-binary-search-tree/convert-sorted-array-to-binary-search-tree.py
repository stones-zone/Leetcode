# -*- coding:utf-8 -*-


# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.sortedArrayToBSTRec(nums, 0, len(nums)-1)
    
    def sortedArrayToBSTRec(self,nums, left, right):
        if left == right:
            return TreeNode(nums[left])
        if left > right:
            return None
        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRec(nums, left, mid - 1)
        node.right = self.sortedArrayToBSTRec(nums, mid + 1, right)
        return node
