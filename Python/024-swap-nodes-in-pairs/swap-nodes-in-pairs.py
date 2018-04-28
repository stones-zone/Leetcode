# -*- coding:utf-8 -*-


# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Note:
#
#
# 	Your algorithm should use only constant extra space.
# 	You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        dummy.next = head
        
        while cur.next and cur.next.next:
            node1, node2, node3 = cur.next, cur.next.next, cur.next.next.next
            cur.next = node2
            node2.next = node1
            node1.next = node3
            cur = node1
        return dummy.next
