# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        
        if not root:return []
        result = []
        queue = collections.deque([(root, sum, [])])
        while queue:
            curr, sum, path = queue.popleft()
            if not curr.left and not curr.right and curr.val == sum:
                result.append(path + [curr.val])
            if curr.left:
                queue.append((curr.left, sum - curr.val, path + [curr.val]))
            if curr.right:
                queue.append((curr.right, sum - curr.val, path + [curr.val]))
        return result
        """
        if not root:return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]
