# -*- coding:utf-8 -*-


# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        """
        if not root:
            return 0
        estack = [root]
        depth = 0
        while estack:
            depth+=1
            new_root = []
            for item in estack:
                if item.left:
                    new_root.append(item.left)
                if item.right:
                    new_root.append(item.right)
            estack = new_root
        return depth
        
