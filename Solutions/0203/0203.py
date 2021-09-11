# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/5 13:38
# File: 0203.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head != None and head.val == val:
            head = head.next
        cur = head
        while cur != None:
            while cur.next != None and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return head
