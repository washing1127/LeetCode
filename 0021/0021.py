# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/6 16:41
# File: 0021.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        ret = None
        f = True
        while l1 and l2:
            if l1.val < l2.val:
                num = l1.val
                l1 = l1.next
            else:
                num = l2.val
                l2 = l2.next
            if ret:
                cur.next = ListNode(num)
                cur = cur.next
            else:
                ret = ListNode(num)
                cur = ret
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return ret