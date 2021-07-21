# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/21 11:55
# File: Offer52.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l = set()
        ca = headA
        cb = headB
        while ca is not None:
            l.add(ca)
            ca = ca.next
        while cb is not None:
            if cb in l: return cb
            cb = cb.next
        return None