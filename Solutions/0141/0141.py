# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/19 18:27
# File: 0141.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = head
        b = head
        while a != None and a.next != None:
            a = a.next.next
            b = b.next
            if a == b:
                return True
        return False