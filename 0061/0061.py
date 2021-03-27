# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/27 23:55
# File: 0061.py
# Desc: 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None: return head
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        num = k%len(l)
        l2 = l[-num:] + l[:-num]
        ret = ListNode(l2[0])
        cur = ret
        for i in l2[1:]:
            cur.next = ListNode(i)
            cur = cur.next
            
        return ret