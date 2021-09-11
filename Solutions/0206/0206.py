# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/2 11:10
# File: 0206.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ret = None
        while head:
            ret, ret.next, head = head, ret, head.next
        return ret