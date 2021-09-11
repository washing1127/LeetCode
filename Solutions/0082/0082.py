# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/25 14:03
# File: 0082.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        a = collections.Counter()
        while head != None:
            a[head.val] += 1
            head = head.next
        li = [k for k,v in a.items() if v==1]
        li.sort()
        if not li: return None
        ret = ListNode(li[0])
        cur = ret
        for i in li[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return ret
