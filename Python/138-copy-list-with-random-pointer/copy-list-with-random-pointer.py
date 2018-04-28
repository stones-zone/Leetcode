# -*- coding:utf-8 -*-


#
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
#
#
# Return a deep copy of the list.
#


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        dummy = RandomListNode(0)
        while cur:
            copy = RandomListNode(cur.label)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next
            
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur, copy_cur = head, dummy
        while cur:
            copy_cur.next = cur.next
            cur.next = cur.next.next
            copy_cur, cur = copy_cur.next, cur.next
        return dummy.next
        

            
