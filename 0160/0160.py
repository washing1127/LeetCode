# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/4 22:36
# File: 0160.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        s = set()
        while cur1 != None:
            s.add(cur1)
            cur1 = cur1.next
        cur2 = headB
        while cur2 != None:
            if cur2 in s:
                return cur2
            cur2 = cur2.next
        return None
