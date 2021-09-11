# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/1/3 下午12:59
desc:
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return None
        n1 = ListNode(None)
        c1 = n1
        n2 = ListNode(None)
        c2 = n2
        while head:
            if head.val < x:
                if c1.val != None:
                    c1.next = ListNode(None)
                    c1 = c1.next
                c1.val = head.val
            else:
                if c2.val != None:
                    c2.next = ListNode(None)
                    c2 = c2.next
                c2.val = head.val
            head = head.next
        if c1.val == None:
            return n2
        elif c2.val == None:
            return n1
        else:
            c1.next = n2
            return n1
