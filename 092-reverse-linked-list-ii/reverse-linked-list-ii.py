# -*- coding:utf-8 -*-


# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween1(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        diff, dummy = n - m + 1, ListNode(0)
        dummy.next = head
        last_unswap = dummy# init first or can't be used
        
        # find last_unswap
        for i in range(m - 1):
            last_unswap = last_unswap.next
        reverse , cur = None, last_unswap.next
        
        # reverse list and find stop position
        for i in range(diff):
            # cur, cur.next, reverse = cur.next, reverse, cur
            # AttributeError: 'NoneType' object has no attribute 'next'
            next =  cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        
        last_unswap.next.next = cur# assign first or last_unswap.next will be changed
        last_unswap.next = reverse# reverse--last swapped position
        
        return dummy.next
    
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for i in range(1, m):
            cur = cur.next
            
        tail = cur.next
        for i in range(m, n):
            if tail is None:
                break
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            
        return dummy.next
