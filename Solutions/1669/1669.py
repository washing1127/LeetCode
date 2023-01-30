# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/01/30 10:42
# File: 1669.py
# Desc: 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ct = 0
        cur1 = list1
        cur2 = list2
        while cur2.next: cur2 = cur2.next
        while cur1:
            if a == 1 and ct == 0:
                nex = cur1.next
                cur1.next = list2
                cur1 = nex
                ct += 1
                if b == 1:
                    cur2.next = cur1.next
                    return list1
            else:
                cur1 = cur1.next
                ct += 1
                if ct == a - 1:
                    nex = cur1.next
                    cur1.next = list2
                    cur1 = nex
                    ct += 1
                if ct == b:
                    cur2.next = cur1.next
                    return list1
