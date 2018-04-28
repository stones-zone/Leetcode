# -*- coding:utf-8 -*-


# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s, cur, count = [], root, 0
        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                count += 1
                if count == k:
                    return cur.val
                cur = cur.right
        return    
        
