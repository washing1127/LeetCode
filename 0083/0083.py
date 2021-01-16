# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/16 19:17
# File: 0083.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if None == head: return head
        doneDic = set()
        ret = ListNode(head.val)
        cur = ret
        doneDic.add(ret.val)
        while head != None:
            if head.val not in doneDic:
                doneDic.add(head.val)
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
            
        return ret