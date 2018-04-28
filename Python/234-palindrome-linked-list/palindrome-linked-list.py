# -*- coding:utf-8 -*-


# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # reverse the first half part
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            reverse, head.next, head = head, reverse, head.next
        # locate the head of tail list according to the nodes num is odd or even
        latter = head.next if fast else head
        is_palindrome = True
        # compare and restore
        while reverse:
            is_palindrome = is_palindrome and reverse.val == latter.val
            reverse.next, head, reverse = head, reverse, reverse.next
            latter = latter.next
        return is_palindrome
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev=None
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            rev,slow.next,slow=slow,rev,slow.next
        if fast:
            slow=slow.next
        while rev and rev.val==slow.val:
            slow=slow.next
            rev=rev.next
        return not rev
            
        
